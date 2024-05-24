# Pyenv
Pyenv is a tool for managing Python versions. It allows you to easily change the global version of Python used on your system, as well as the specific version of each project you work on.

This is useful for ensuring compatibility with multiple projects that may require different versions of Python, as well as formalizing the version used for other collaborators.

## Documentation
You can find the full documentation [here](https://github.com/pyenv/pyenv).

## Main commands
### 1. Installing Python Versions
- Lists all versions available for installation
```py
pyenv install --list
```

- Installs a specific version of Python.
```py
pyenv install [version]
```

### 2. Version Management
- Shows all installed Python versions
```py
pyenv versions
```

- Defines the version of Python to be used globally on the system.
```py
pyenv global [version]
```

- Sets the Python version to be used locally in a specific directory.
```py
pyenv local [version]
```

### 3. Activate Virtual Env in the Terminal
- Activating the virtual environment (Windows)
```py
source .venv\Scripts\activate
```

- Activating the virtual environment (Linux)
```py
source .venv/bin/activate
```