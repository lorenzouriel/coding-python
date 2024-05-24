# Taskipy
Taskipy is a task execution tool for Python, allowing the automation of commands and scripts through a single configuration file: **pyproject.toml**

## Documentation
You can find the full documentation [here](https://github.com/taskipy/taskipy).

## Basic Configuration
It provides a simple and elegant way to organize and manage project tasks, such as build, test and deploy, in an easy and repeatable way:
```py
[tool.taskipy.tasks]
test = "pytest -v"
lint = "flake8 src/tests/"
format = "blue . && isort ."
```

**In this example:**
- `test` runs tests using pytest with verbose output.
- `lint` checks the code quality in the src/tests/ directory using flake8.
- `format` formats the code using black and isort.

**Another example of Taskipy:**
```py
[tool.poetry]
name = "dataprojectstarterkit"
version = "0.1.0"
description = ""
authors = ["Luciano Filho <lvgalvaofilho@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "3.11.2"
faker = "^19.6.2"
pandas = "^2.1.1"
pytest = "^7.4.2"
openpyxl = "^3.1.2"
isort = "^5.12.0"
pre-commit = "^3.4.0"
black = "^23.9.1"
mkdocstrings = "^0.23.0"
pip-audit = "^2.6.1"
taskipy = "^1.12.0"

[tool.isort]
profile = "black"
known_third_party = []
[tool.poetry.group.dev.dependencies]
mkdocs = "^1.5.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.taskipy.tasks]
format = """
isort .
black .
"""
kill = "kill -9 $(lsof -t -i :8000)"
test = "pytest -v"
run = "python app/main.py"
doc = "mkdocs serves"
```

## Getting Started
To get started with Taskipy, follow these steps:

**1. Install Taskipy:**
```sh
poetry add taskipy --dev
```

**2. Configure Tasks:**
Add your tasks to the pyproject.toml file under the `[tool.taskipy.tasks]` section.

**3. Run Tasks:**
Use the poetry run task <task-name> command to execute your tasks. For example:
```sh
poetry run task test
```
By integrating Taskipy into your Python project, you can streamline your workflow, improve productivity, and maintain a clean and organized codebase.