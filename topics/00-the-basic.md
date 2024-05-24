# What Is Python?
Python is an Open Source programming language, considered high-level, that is, more similar to human language.

It was created by Guido Van Russen in 1991, having its name originating from a Monty Python TV series.


## Primitive Types in Python:
1. **Integer (int):** Represents whole numbers.
```python
x = 5
```

2. **Float (float):** Represents decimal numbers.
```python
y = 3.14
```

3. **String (str):** Represents text.
```python
name = "John"
```

4. **Boolean (bool):** Represents True or False.
```python
is_student = True
```


## Data Output:

To output data in Python, you can use the `print()` function. 
```python
# Printing variables
print(x)  # Output: 5

print(y)  # Output: 3.14

print(name)  # Output: John

print(is_student)  # Output: True

# You can also print text directly
print("Hello, World!")
```

Python uses **dynamic typing, which means you don't need to declare the type of a variable explicitly.** The interpreter determines the type based on the value assigned.

## Data Input:

To input data in Python, you can use the `input()` function. This function allows users to enter data interactively from the console.

```python
# Taking input from the user
x = int(input("Enter a number: "))  # User input: 10
y = float(input("Enter a decimal number: "))  # User input: 3.14
name = str(input("Enter your name: "))  # User input: Lorenzo
is_student = bool(input("Are you a student? (yes/no): "))  # User input: yes

# Printing the input values
print("Number entered:", x)  # Output: Number entered: 10
print("Decimal number entered:", y)  # Output: Decimal number entered: 3.14
print("Name entered:", name)  # Output: Name entered: Lorenzo
print("Is student?", is_student)  # Output: Is student? True
```

***Note:** When using `input()` without, Python treats all input as strings. Therefore, you may need to convert the input to the appropriate data type using functions like `int()`, `float()`, or `bool()` depending on your requirements.*


## Arithmetic Operators
In Python, arithmetic operators allow you to perform mathematical operations on numeric values. Here are the common arithmetic operators:

1. **Addition:** Adds two values together.
```python
a = 5
b = 3
result = a + b
print(result)  # Output: 8
```

2. **Subtraction:** Subtracts the right operand from the left operand.
```python
a = 7
b = 4
result = a - b
print(result)  # Output: 3
```

3. **Multiplication:** Multiplies two values.
```python
a = 3
b = 2
result = a * b
print(result)  # Output: 6
```

4. **Division:** Divides the left operand by the right operand, result is always a float.
```python
a = 8
b = 2
result = a / b
print(result)  # Output: 4.0
```

5. **Integer Division:** Divides the left operand by the right operand, result is the floor of the division (truncates the decimal part).
```python
a = 8
b = 3
result = a // b
print(result)  # Output: 2
```

6. **Modulus - Resto da Divisão:** Returns the remainder of the division of the left operand by the right operand.
```python
a = 8
b = 3
result = a % b
print(result)  # Output: 2
```

7. **Exponentiation:** Raises the left operand to the power of the right operand.
```python
a = 2
b = 3
result = a ** b
print(result)  # Output: 8
```

**Order of Precedence:**
These operators follow the usual rules of arithmetic. You can use parentheses to control the order of operations.
```python
result = (5 + 3) * 2
print(result)  # Output: 16
```

The Order
```
1.  ( )
2.  **
3.  *   /   //    %
4.  +   -
```

---
# Notes to Get Started
- **Py** limit is the memory

- `end = ' '` → Don't broke the line

- `/n` → Add New Line

- `#` → To make comments

- `==` → Equal to

- `Cntl + Space` → Check ssemblies

- `<built in>` → Existence assemblies

- `Pypi, Python.org` → Search for libs

- `nan` → Is the NULL value for Python

- **PEP 8**
    - PEP 8 is a style guide for Python code. 
    - This document provides the coding conventions for writing code in Python. Coding conventions are about indentation, formatting, tabs, maximum line length, imports organization, line spacing etc. 
    - We use PEP 8 to bring consistency in our code, consistency it is easier for other developers to read the code.

- **isort**
    - isort is a command-line tool and Python library that organizes imports from a Python file according to PEP8 conventions. 
    - It helps ensure that imports are organized in a readable and consistent way, making code easier to maintain.
        - Install: `pip install isort`
        - Run: `isort .`, `isort basic_data_output.py`, `isort basic_data_input.py, basic_data_output.py`
        - View changes: `isort mypythonfile.py --diff`

- **black**
    - black is a Python code formatting tool that applies a consistent and semantic formatting style to source code. 
    - It automatically formats Python code according to its predefined rules, thus ensuring that the code is uniform and easy to read without the need for code style debates.
        - Install: `pip install black`
        - Install for Jupyter Notebooks: `pip install "black[jupyter]"`
        - Run: `black {source_file_or_directory}`, `python -m black {source_file_or_directory}`

- **blue**
    - blue is a Python code formatting tool that applies a consistent and semantic formatting style to source code. blue was inspired in black
        - Install: `pip install blue`
        - Install for Jupyter Notebooks: `pip install "blue[jupyter]"`
        - Run: `blue {source_file_or_directory}`, `python -m blue {source_file_or_directory}`

- **pydocstyle**
    - pydocstyle is a tool that checks the style of docstrings in Python code. 
    - It follows the conventions defined in PEP 257, which outlines guidelines for writing docstrings in Python. pydocstyle helps ensure that your Python code documentation is well formatted and consistent across your project.
        - Install: `pip install pydocstyle`
        - Run: `pydocstyle test.py`

- **flake8**
    - flake8 is a Python code checking tool that checks code for errors, style, and maintenance issues. 
    - It integrates several other tools such as pycodestyle (formerly known as pep8), pyflakes, and McCabe to provide a comprehensive analysis of Python code for potential issues.
        - Install: `pip install flake8`
        - Run: `flake8 path/to/code/to/check.py`, `flake8 path/to/code/`

- **pip-audit**
    - Is a tool that checks for known vulnerabilities in Python packages installed in your virtual environment. 
    - It checks the National Vulnerability Database (NVD) for vulnerability information and compares it to the packages installed in your environment.
        - Install: `pip install pip-audit`
        - Run: `pip-audit --help`, `python -m pip_audit --help`, `pip-audit -r ./requirements.txt`, `pip-audit .`
        