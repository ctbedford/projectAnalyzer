
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

    --files: Specify specific files to analyze.
    --no-content: Exclude file content from the analysis.
    --exclude-dirs: Additional directories to exclude (comma-separated list).
    --include-types: File types to include (comma-separated list).
    --content-preview: Include only a preview of file content (first 10 lines).
    --ignore-large-files: Ignore files larger than the specified size.
    --max-file-size: Maximum file size (in bytes) to process.

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
