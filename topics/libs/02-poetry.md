# Poetry
Poetry is a dependency management and packaging tool in Python. It allows you to declare the libraries your project depends on and how it will manage (install/update) them for you. 

Additionally, it follows **PEP 517/518**, describing all project metadata through the **pyproject.toml file**

## Documentation
You can find the full documentation [here](https://python-poetry.org/docs/)

## Main commands
### 1. Initialization and Configuration
- Start a new project or configure an existing one using a wizard to create a pyproject.toml.
```py
poetry init
```

### 2. Dependency Management
- Added a new package as dependency and installation.
```py
poetry add [package]
```

- Remove a dependency from the project.
```py
poetry remove [package]
```

- Shows installed dependencies.
```py
poetry show
```

### 3. Virtual Environment
- Create and log into a shell within the virtual environment
```py
poetry shell
```

- Define the Python version to be used by the project's virtual environment
```py
poetry env use [python_version]
```

Here are some main characteristics of Poetry:
- **Dependency Management:** Poetry uses the pyproject.toml file to define project metadata and dependencies. It automatically manages installation and dependency resolution.
- **Virtual Environments:** Poetry creates and manages virtual environments for your projects, isolating their dependencies from the global Python environment.
- **Package Building:** Poetry simplifies the process of packaging your Python project into a distributable format (e.g. a wheel or source code distribution).
- **Scripting:** Poetry allows you to define and execute custom scripts for various tasks, making it easier to automate common project-related tasks.
- **Consistency:** Poetry aims to provide a consistent and reliable workflow for Python projects, addressing some of the complexities that can arise when using other tools.