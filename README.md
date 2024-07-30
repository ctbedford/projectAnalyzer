
# ProjectAnalyzer

ProjectAnalyzer is a tool designed to analyze the structure of software projects. It scans the directory of a given project and provides detailed insights into the project's files, directories, and their contents. This tool is particularly useful for developers who need to quickly understand the layout and components of a new codebase.
Features

- Directory and File Analysis: Provides a comprehensive overview of the project's directory structure.
- File Content Preview: Offers an option to preview the contents of text files.
- Key File Identification: Highlights key files in frameworks like Django and React.
- Exclusion Filters: Allows exclusion of certain directories and file types.
- Customizable Output: Generates JSON output detailing the analyzed project structure.

## Installation

To use ProjectAnalyzer, you need Python 3 installed on your system. You can clone the repository and set up a symbolic link for easy command-line access.

- Clone the Repository:

    ```bash
    git clone https://github.com/ctbedford/projectAnalyzer.git
    ```


- Set Up Symbolic Link (Optional):

```bash
sudo ln -s /path/to/projectAnalyzer/project_analyzer.py /usr/local/bin/projectanalyzer

```


- Replace /path/to/projectAnalyzer/ with the actual path to your cloned repository.

- Make Script Executable (if not already):

```bash
    chmod +x /path/to/projectAnalyzer/project_analyzer.py

```


## Usage

To analyze a project, run the projectanalyzer command followed by the directory path you want to analyze. Here are some common options:

```bash
projectanalyzer /path/to/project --output /path/to/output.json [OPTIONS]

```


Options

    -h, --help            show this help message and exit
    --output OUTPUT       Output file for analysis results (default: ./project_structure.json)
                          Specify a valid file path with .json extension.
    --files [FILES ...]   Specific files to analyze. Can be file names or relative paths.
                          If not specified, all files matching --include-types will be analyzed.
    --no-content          Exclude file content from the analysis. Reduces output size but provides less detail.
    --exclude-dirs [EXCLUDE_DIRS ...]
                          Additional directories to exclude from analysis.
                          Default excluded: node_modules, venv, .git, __pycache__, migrations, build, .mypy_cache
                          Specify as space-separated list, e.g., --exclude-dirs tests docs
    --include-types [INCLUDE_TYPES ...]
                          File types to include in the analysis.
                          Default: .py .js .jsx .ts .tsx .json .yml .yaml .md .html .css
                          Specify as space-separated list with leading dot, e.g., --include-types .py .js .ts
    --content-preview     Include only a preview of file content (first 10 lines) instead of full content.
                          Useful for reducing output size while still providing some content insight.
    --ignore-large-files  Ignore files larger than the size specified by --max-file-size.
                          Useful for excluding large binary or data files from analysis.
    --max-file-size MAX_FILE_SIZE
                          Maximum file size in bytes to process (default: 1048576 bytes, i.e., 1 MB)
                          Files larger than this will be ignored if --ignore-large-files is set.
                          Acceptable range: 1 to 1073741824 (1 GB)

Example

Analyze a project and save the output to output.json:

```bash
projectanalyzer /home/user/my_project --output /home/user/output.json --exclude-dirs node_modules,.git --content-preview

```


Contribution

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
License

ProjectAnalyzer is licensed under the MIT License. See the LICENSE file for more information.
Contact

For any inquiries or issues, please contact [Tyler Bedford] at [tybed7@icloud.com].

Feel free to customize this template based on your specific project details, contact information, and contribution guidelines. This README provides a solid foundation, ensuring users can quickly understand and start using your tool.
