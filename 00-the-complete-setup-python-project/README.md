## 🗂️ Introduction to "The Complete Setup Python Project"
The idea of ​​this repository is to have a **guide on how to structure a good Python project from scratch and why structure it that way**

This README.md will be a step-by-step guide to the flow of any project


## 💥Steps
### **1. Git & GitHub** - Git is a tool for code versioning and GitHub serves as a repository for this code

- Create a repository on GitHub and run the following commands
```bash
echo "# the-complete-setup-python-project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/lorenzouriel/the-complete-setup-python-project.git
git push -u origin main
```

- Or, clone the repository
```bash
git clone https://github.com/lorenzouriel/the-complete-setup-python-project
cd the-complete-setup-python-project
```

- Create new branch
```bash
git branch # Check branch

git branch dev # Create dev branch

git checkout dev # Change to dev branch

git push --set-up-stream  # Push new branch
```

### **2. Pyenv** - Tool to manage Python versions

- Initialization
```python
pyenv install 3.11.5  # Install the correct python version with `pyenv`
pyenv local 3.11.5    # Configure the correct python version with `pyenv`
```

- Create a virtual env with pip
```python
python -m venv .venv  # Create the .venv with python

.venv\Scripts\activate     # Activate .venv Windows
source .venv/bin/activate  # Activate .venv Linux
```

- Installing a libs
```python
pip install streamlit
```

- Managing Libs
```python
pip freeze > requirements.txt     # Create a list of all dependencies in the .venv

pip install -r requirements.txt   # Install the list of dependencies in the .venv
```

- Other Commands with Pyenv
```python
pyenv install --list # List all python versions

pyenv versions # Show all installed python versions

pyenv global [version] # Define the Python global versions
```

### **3. Poetry** - Is a tool for dependency management and packaging in Python
He follows the PEP 517/518, describing all the metadata of the project through file pyproject.toml

- Initialization
```python
poetry init  # Start a new project or configures an existing one through a wizard to create a pyproject.toml
```

- Virtual Env
```python
poetry shell  # Create and log into a shell within the virtual environment
poetry env use 3.11.5  # Sets the version of Python to be used by virtual project environment
```

- Manage dependencies (Will be create a poetry.lock and all the dependencies will be added to pyproject.toml)
```python
poetry add pandas # Add dependencies
poetry remove pandas # Remove dependencies
poetry show # Show dependencies
```

---
### Install the dependencies below using pip or poetry

- poetry example
```python
poetry add taskipy   # Automate tasks with one command in the pyproject.toml

poetry add pytest    # Run unitary, integrational and functional tests 

poetry add mkdocs    # MkDocs is a fast tool and simple way to create websites documentation from written files in Markdown.
poetry add mkdocs-material # Most used the for Markdown
poetry add 'mkdocstrings[python]' # Adds mkdocstrings with support for Python
poetry add 'mkdocs-mermaid2-plugin' # Plugin to create Flowchart using mermaid codes


poetry add isort   # organizes imports from a Python file according to PEP8 conventions
poetry add blue    # A Python code formatterwhich will reformat the code to conform to PEP 8
```

- Example of taskipy in pyproject.toml
```python
[tool.taskipy.tasks]
run = "streamlit run src/app.py"
test = "pytest tests -v"
format = "blue . && isort ."
docs = "mkdocs serve"


task run
tast test
task format
task docs
```

- Create a new .gitignore and copy the [toptal](https://www.toptal.com/developers/gitignore/api/python) gitignore
```bash
New-Item .gitignore   # Power Shell

type nul > .gitignore # cmd

touch .gitignore      # Mac and Linux

cat .gitignore        # Mac and Linux
```
---

- **Now, go coding, that's all folks!**