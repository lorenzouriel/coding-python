# Folders Structures
**1. SRC/APP/[Package Name]**
- **Purpose:** Contains the source code of the project

**2. TESTS**
- **Purpose:** Stores automated tests to verify the correctness of the code in SRC

**3. DOCS**
- **Purpose:** Contains project documentation, possibly written using tools like Sphinx.

**4. SCRIPTS**
- **Purpose:** May contain useful scripts for automating tasks such as installation, compilation, test execution, among others.

# Common Files
**.gitignore**
- **Purpose:** List of files and directories that Git should ignore when committing.

**README.md**
- **Purpose:** A markdown file that provides basic information about the project, such as its description, usage mode and installation instructions.

**.pre-commit-config.yaml**
- **Purpose:** Configuration for the pre-commit tool, which helps manage and maintain pre-commit hooks.

**.python-version**
- **Purpose:** Specifies the version of Python used in the project, often used in conjunction with version managers such as pyenv

**.github/workflows**
- **Purpose:** Contains the workflow scripts for GitHub Actions, enabling the automation of CI/CD pipelines directly in GitHub

**pyproject.toml**
- **Purpose:** A configuration file for Python project build tools such as Poetry or PEP 517/518 that contains project metadata and dependencies

**requirements.txt**
- **Purpose:** A list of project dependencies for installing with pip, although pyproject.toml is becoming more common.

# Code Standards
Maintaining code standards in Python is critical to ensuring code readability, consistency, and, in some cases, security.

Here are 12 libraries and tools that can help you maintain code standards, adhering to **PEPs (Python Enhancement Proposals), checking typography, docstrings, and security concerns:**

## Main Libraries
**1. `flake8`: Linting**
- Description: Checks code against PEP8 and can be extended with plugins to check against more conventions.

**2. `black`: Code Formatting**
- Description: Formats code consistently and adheres to "The Black Code" style.

**3. `mypy`: Type Checking**
- Description: Checks static typing in Python to detect type errors before code execution.

**4. `pylint`: Linting**
- Description: Lint tool that checks adherence to the style guide and can be customized to meet your needs.

**5. `pydocstyle`: Docstring Check**
- Description: Checks the conformity of docstrings with the PEP257 convention.

**6. `bandit`: Security**
- Description: Looks for common security issues through static code analysis.

**7. `isort`: Import Organization**
- Description: Organizes imports in an orderly and grouped manner.

**8. `blue`: Code Formatting** 
- Description: A Python code formatter that will reformat code to conform to PEP 8, with some deviations.

**9. `pip-audit`: Security** 
- A tool for checking installed dependencies to search for and fix known vulnerabilities

**10. `Prospector`: Static Code Analysis** 
- Description: A tool that brings together several others (including flake8 and mypy) to perform a static analysis of the code and offer suggestions for improvements.

**11. `SonarQube`: Analysis and Quality**
- SonarQube is a robust platform used for continuous inspection of code quality to detect bugs.

**12. `Radon`: Complexity Analysis** 
- Radon is a Python tool for obtaining various code metrics, including complexity and a code maintainability rank.

## Python Tips
`isort`
- isort is a command-line tool and Python library that organizes imports from a Python file according to PEP8 conventions. It helps ensure that imports are organized in a readable and consistent way, making code easier to maintain.

`black`
- Black is a Python code formatting tool that applies a consistent and semantic formatting style to source code. It automatically formats Python code according to its predefined rules, thus ensuring that the code is uniform and easy to read without the need for code style debates.

`pydocstyle`
- pydocstyle is a tool that checks the style of docstrings in Python code. It follows the conventions defined in PEP 257, which outlines guidelines for writing docstrings in Python. pydocstyle helps ensure that your Python code documentation is well formatted and consistent across your project.

`flake8`
- flake8 is a Python code checking tool that checks code for errors, style, and maintenance issues. It integrates several other tools such as pycodestyle (formerly known as pep8), pyflakes, and McCabe to provide a comprehensive analysis of Python code for potential issues.

`pep8`
- pep8 is a style guide for Python code that describes best practices for writing readable and consistent code. PEP8 defines conventions for code formatting, variable naming, use of white space, among other guidelines. Tools like pycodestyle and flake8 help you apply PEP8 rules to Python code.

`pip-audit`
- is a tool that checks for known vulnerabilities in Python packages installed in your virtual environment. It checks the National Vulnerability Database (NVD) for vulnerability information and compares it to the packages installed in your environment.