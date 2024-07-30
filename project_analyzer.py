#!/usr/bin/env python3
import os
import json
from typing import Dict, List, Union
import argparse

DEFAULT_EXCLUDED_DIRS = {'node_modules', 'venv', '.git',
                         '__pycache__', 'migrations', 'build', '.mypy_cache'}
DEFAULT_IMPORTANT_FILE_TYPES = {'.py', '.js', '.jsx', '.ts',
                                '.tsx', '.json', '.yml', '.yaml', '.md', '.html', '.css'}
KEY_FILES_DJANGO = {'models.py', 'views.py', 'urls.py',
                    'settings.py', 'serializers.py', 'forms.py', 'admin.py'}
KEY_FILES_REACT = {'.jsx', '.js'}


def analyze_project(root_dir: str, specific_files: List[str] | None = None, include_content: bool = True,
                    exclude_dirs: List[str] | None = None, include_types: List[str] | None = None,
                    content_preview: bool = False, ignore_large_files: bool = False,
                    max_file_size: int = 1024 * 1024) -> Dict[str, Union[List[Dict[str, str]], Dict[str, str]]]:
    project_structure = {"files": [], "directories": [], "analysis": {}}
    file_count = 0

    excluded_dirs = set(exclude_dirs or []) | DEFAULT_EXCLUDED_DIRS
    included_types = set(include_types or DEFAULT_IMPORTANT_FILE_TYPES)

    if specific_files:
        for file_name in specific_files:
            found_files = find_file(root_dir, file_name)
            for full_path in found_files:
                rel_path = os.path.relpath(full_path, root_dir)
                file_info = analyze_file(
                    full_path, rel_path, include_content, content_preview, ignore_large_files, max_file_size)
                if file_info:
                    project_structure["files"].append(file_info)
                    file_count += 1
    else:
        for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
            dirnames[:] = [d for d in dirnames if d not in excluded_dirs]
            rel_path = os.path.relpath(dirpath, root_dir)
            if rel_path != '.':
                project_structure["directories"].append({
                    "path": rel_path,
                    "name": os.path.basename(dirpath)
                })
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                rel_file_path = os.path.relpath(file_path, root_dir)
                if os.path.splitext(filename)[1] in included_types:
                    file_info = analyze_file(
                        file_path, rel_file_path, include_content, content_preview, ignore_large_files, max_file_size)
                    if file_info:
                        project_structure["files"].append(file_info)
                        file_count += 1
                        if file_count % 100 == 0:
                            print(f"Processed {file_count} files...")

    project_structure["analysis"] = analyze_project_structure(
        project_structure)
    print(f"Total files processed: {file_count}")
    return project_structure


def find_file(root_dir: str, file_name: str) -> List[str]:
    found_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in DEFAULT_EXCLUDED_DIRS]
        if file_name in filenames:
            found_files.append(os.path.join(dirpath, file_name))
    return found_files


def analyze_file(file_path: str, rel_file_path: str, include_content: bool, content_preview: bool,
                 ignore_large_files: bool, max_file_size: int) -> Dict[str, str] | None:
    file_size = os.path.getsize(file_path)
    if ignore_large_files and file_size > max_file_size:
        return None

    file_info = {
        "name": os.path.basename(file_path),
        "path": rel_file_path,
        "size": file_size,
        "type": get_file_type(file_path)
    }

    if include_content:
        content = get_file_content(file_path, content_preview)
        if content:
            file_info["content"] = content
            file_info["line_count"] = len(content.splitlines())

    return file_info


def get_file_type(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    if ext in DEFAULT_IMPORTANT_FILE_TYPES:
        return "text"
    elif ext in ['.jpg', '.png', '.gif', '.svg', '.ico']:
        return "image"
    else:
        return "other"


def get_file_content(file_path: str, preview: bool) -> str | None:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if preview:
                # First 10 lines
                return ''.join(f.readline() for _ in range(10))
            else:
                return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return None


def analyze_project_structure(project_structure: Dict) -> Dict[str, str]:
    analysis = {}

    # Check for Django
    if any(f["name"] == "manage.py" for f in project_structure["files"]):
        analysis["framework"] = "Django"
        analysis["django_apps"] = [d["name"] for d in project_structure["directories"] if "apps.py" in [
            f["name"] for f in project_structure["files"] if f["path"].startswith(d["path"])]]

    # Check for React
    if any(f["name"] == "package.json" and "react" in f.get("content", "") for f in project_structure["files"]):
        analysis["frontend"] = "React"

    return analysis


def main():
    parser = argparse.ArgumentParser(description="Analyze project structure")
    parser.add_argument("root", help="Root directory of the project")
    parser.add_argument("--output", help="Output file for analysis results",
                        default="./project_structure.json")
    parser.add_argument("--files", nargs="*", help="Specific files to analyze")
    parser.add_argument("--no-content", action="store_true",
                        help="Exclude file content from the analysis")
    parser.add_argument("--exclude-dirs", nargs="*",
                        help="Additional directories to exclude (default: node_modules, venv, .git, __pycache__, migrations, build, .mypy_cache)")
    parser.add_argument("--include-types", nargs="*",
                        help="File types to include (default: .py, .js, .jsx, .ts, .tsx, .json, .yml, .yaml, .md, .html, .css)")
    parser.add_argument("--content-preview", action="store_true",
                        help="Include only a preview of file content (first 10 lines)")
    parser.add_argument("--ignore-large-files", action="store_true",
                        help="Ignore files larger than specified size")
    parser.add_argument("--max-file-size", type=int, default=1024*1024,
                        help="Maximum file size in bytes to process (default: 1048576 bytes)")

    args = parser.parse_args()

    project_structure = analyze_project(
        args.root,
        args.files,
        not args.no_content,
        args.exclude_dirs,
        args.include_types,
        args.content_preview,
        args.ignore_large_files,
        args.max_file_size
    )

    with open(args.output, 'w') as f:
        json.dump(project_structure, f, indent=2)

    print(f"Project structure analysis saved to {args.output}")
    print(f"Number of files analyzed: {len(project_structure['files'])}")


if __name__ == "__main__":
    main()
