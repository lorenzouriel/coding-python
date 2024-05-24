# Pre-commit
Pre-commit is a Git hook framework designed to help maintain code quality by ensuring that automated reviews, such as code formatting and lint checks, are performed before each commit. This tool prevents code that does not meet specific standards from being committed. For more details, visit the official Pre-commit website.

The primary goal of Pre-commit is to prevent code that does not adhere to established standards from being committed to the repository. This ensures that only high-quality, well-formatted code is integrated into the project.

Pre-commit automates the process of checking and correcting code before it is committed. This saves developers time by automating routine checks and corrections, allowing them to focus on tasks that generate value, rather than spending time on formatting and other repetitive tasks.

### Installation
To install and configure Pre-commit with this configuration, follow these steps:

**1. Install Pre-commit using Poetry:**
```sh
poetry add pre-commit
```

**2. Install Pre-commit hooks:**
```sh
pre-commit install
```

**3. Run Pre-commit manually on all files (optional but useful for the first time):**
```sh
pre-commit run --all-files
```

### Configuration
To set up Pre-commit, you need to define your automatic checks and fixes in the ``.pre-commit-config.yaml`` file located in your repository. This file specifies the rules and hooks that Pre-commit will enforce.

### Example
```yml
# .pre-commit-config.yaml

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml

  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.11.0
    hooks:
      - id: isort
```

**Explanation of the Configuration:**
**1. pre-commit-hooks:**
- `trailing-whitespace:` Removes trailing whitespace.
- `end-of-file-fixer:` Ensures files end with a newline.
- `check-yaml:` Checks YAML files for syntax errors.
- `black:` A Python code formatter that ensures consistent code style.
- `flake8:` A tool for checking Python code against style conventions and logical errors.
- `isort:` A Python utility for sorting imports to ensure a consistent import order.