# Project: API Data Processing

## Learning Objectives
By the end of this project, you are expected to comprehend the following concepts without external assistance:

1. **Bash Scripting Scope:** Understanding the appropriate use cases and limitations of Bash scripting.

2. **API Understanding:**
   - Recognition of an API (Application Programming Interface).
   - Understanding REST APIs and their role in web development.
   - Awareness of microservices architecture.

3. **Data Formats:**
   - Familiarity with CSV (Comma-Separated Values) format.
   - Familiarity with JSON (JavaScript Object Notation) format.

4. **Python Coding Conventions:**
   - Adherence to Pythonic naming styles for packages, modules, classes, variables, functions, and constants.
   - Recognition of the significance of CapWords or CamelCase in Python.

5. **Copyright and Plagiarism:**
   - Understanding the importance of original work.
   - Strict adherence to copyright rules and prohibition of plagiarism.

## Requirements
### General
1. **Editors:** Allowed editors include vi, vim, and emacs.
2. **Execution Environment:** All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
3. **File Endings:** All files should end with a new line.
4. **Shebang Line:** The first line of all files should be exactly `#!/usr/bin/python3`.
5. **Library Organization:** Libraries imported in Python files must be organized in alphabetical order.
6. **README File:** A README.md file at the root of the project folder is mandatory.
7. **Code Style:** Code should follow the pycodestyle (version 2.8.*) guidelines.
8. **File Executability:** All files must be executable.
9. **File Length:** The length of your files will be tested using `wc`.
10. **Documentation:** All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)`).
11. **Dictionary Access:** Use `get` to access dictionary values by key.
12. **Module Execution:** Code should not be executed when imported (`if __name__ == "__main__":`).

### Tasks
#### Task 0: Gather Data from an API
- Write a Python script using the `urllib` or `requests` module that, for a given employee ID, returns information about their TODO list progress.
- Display the information in a specified format.

#### Task 1: Export to CSV
- Extend the script from Task 0 to export data to a CSV file.
- Records should include tasks owned by the employee, and the format should be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`.
- The file name should be: `USER_ID.csv`.

#### Task 2: Export to JSON
- Extend the script from Task 0 to export data to a JSON file.
- Records should include tasks owned by the employee, and the format should be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`.
- The file name should be: `USER_ID.json`.

#### Task 3: Dictionary of List of Dictionaries
- Extend the script from Task 0 to export data to a JSON file.
- Records should include tasks from all employees, and the format should be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`.
- The file name should be: `todo_all_employees.json`.

## Project Structure
- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- **Directory:** 0x15-api

## Files
1. **Task 0 Script:**
   - File: 0-gather_data_from_an_API.py

2. **Task 1 Script:**
   - File: 1-export_to_CSV.py

3. **Task 2 Script:**
   - File: 2-export_to_JSON.py

4. **Task 3 Script:**
   - File: 3-dictionary_of_list_of_dictionaries.py

## Usage Examples
```bash
# Task 0
python3 0-gather_data_from_an_API.py 2

# Task 1
python3 1-export_to_CSV.py 2
cat 2.csv

# Task 2
python3 2-export_to_JSON.py 2
cat 2.json

# Task 3
python3 3-dictionary_of_list_of_dictionaries.py
cat todo_all_employees.json
```
