# Functions, Interactive Help, Docs Strings, Modules and Packages
In Python, a function is a block of organized, reusable code that performs a specific task. 

Functions help modularize your code, making it more readable, maintainable, and reusable.

**1. Defining a Function:** You can define a function using the `def` keyword, followed by the function name and a pair of parentheses. If the function takes parameters, they are listed inside the parentheses.
```python
def greet(name):
    """This function prints a greeting."""
    print(f"Hello, {name}!")
```

In this example:
- `greet` is the function name.
- `name` is a parameter (input) to the function.
- The `triple-quoted` string is a `docstring`, providing a brief description of the function.


**2. Calling a Function:** Once a function is defined, you can call it to execute the code inside the function.
```python
greet("Lorenzo")
# Output: Hello, Lorenzo!
```


**3. Returning Values:** Functions can return values using the `return` statement. The returned value can be assigned to a variable or used in expressions.
```python
def add(x, y):
    """This function returns the sum of two numbers."""
    return x + y

result = add(3, 5)
print(result)
# Output: 8
```

**4. Default Parameters:** You can assign default values to function parameters. If a value is not provided when calling the function, the default value is used.
```python
def power(base, exponent=2):
    """This function calculates the power of a number with a default exponent of 2."""
    return base ** exponent

print(power(3))
# Output: 9

print(power(3, 3))
# Output: 27
```

**4. Optional Parameters:** You can assign optional values to function parameters.
```python
def my_sum(a, b, c=0 or c=false):
    """This function calculates the power of a number with a optional parameter in C""" 
    sum = a + b + c
    return sum
 
print(my_sum(4, 5)) 
# Output: 9
```

**5. Variable Number of Arguments:** You can use the `*args` syntax to allow a variable number of arguments in a function.
```python
def average(*numbers):
    """This function calculates the average of a variable number of arguments."""
    return sum(numbers) / len(numbers)

print(average(1, 2, 3, 4, 5))
# Output: 3.0
```

**6. Keyword Arguments:** You can use the `**kwargs` syntax to allow a variable number of keyword arguments.
```python
def person_info(**kwargs):
    """This function prints information about a person."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="John", age=30, city="New York")
# Output:
# name: John
# age: 30
# city: New York
```

## Interactive Help and Docs Strings
In Python, interactive help and docstrings are essential tools for understanding and documenting code.

### Interactive Help:
**1. Using `help()` function:** The `help()` function provides interactive help for Python objects, functions, modules, etc. You can use it in the Python interpreter or within your scripts.
```python
help(print)
```
*This will display information about the `print` function.*

**2. Using ? in Jupyter Notebooks:** In Jupyter Notebooks, you can also use the question mark ? to get help on an object.
```python
print?
```
*This will display a help window with information about the print function.*

### Docstrings:
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. **It is used to document the purpose and usage of the code.**

**1. Structure:** It´s important to follow a default structure like:
``` python
def example(parameter)
    """
    Function Description: Brief description

    Function Paramaters:
    - number (int or float): The input number.

    Function Return:
    - int or float: The square of the input number.
    """
    return parameter + "Love You"
```

- Example:
```python
def square(number):
    """
    This function returns the square of a number.

    Parameters:
    - number (int or float): The input number.

    Returns:
    - int or float: The square of the input number.
    """
    return number ** 2
```

**2. Accessing Docstrings:**

- Using help() function:
```python
help(square)
```

- Using __doc__ attribute:
```python
print(square.__doc__)
```


## Modules and Packages
A module **is a file containing Python definitions and statements.**

The file name is the module name with the suffix `.py` appended. Modules allow you to logically organize your Python code into reusable files. 

**You can use the functions, variables, and classes defined in a module in other Python files by importing them.**

Here's a simple example:

**1. Creating a Module:** Let's create a module named  `my.module.py` with a simple function:
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"
```

**2. Using the Module:**
Now, in another Python file or interactive session, you can import and use the module:
```python
# main.py

# Importing the entire module
import my_module

result = my_module.greet("Lorenzo")
print(result)  # Output: Hello, Lorenzo!
```

- *To import a module correctly, you need to create an empty Python file in the folder named: `__init__.py`*

- *The `__init__.py` file in Python **is used to indicate that a directory should be treated as a Python package.** This file can be empty or can contain initialization code for the package. Read more below!*


**3. You can also import specific functions or variables from a module:**
```python
# Importing a specific function
from my_module import greet

result = greet("Lorenzo")
print(result)  # Output: Hello, Lorenzo!
```

**4. You can use the as keyword to provide an alias when importing:**
```python
# Importing with an alias
import my_module as mm

result = mm.greet("Charlie")
print(result)  # Output: Hello, Charlie!
```

**5. Modules can also have executable code that only runs when the module is run as the main program, using the `if __name__ == "__main__":`**
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"
if __name__ == "__main__":
    # This code runs only when the module is run as the main program
    print("This is my_module.")
```


### Packages:
A package is a way of organizing related modules into a single directory hierarchy. 

A package is a collection of Python modules organized in directories. It must contain a special file named `__init__.py` (which can be empty) to be recognized as a package.

- **Example:** Suppose you have a package structure like this:
```
my_package/
|-- __init__.py
|-- module1.py
|-- module2.py
```

- You can import modules from the package like this:
```python
# main.py
from my_package import module1, module2

result1 = module1.some_function()

result2 = module2.another_function()

print(result1, result2)
```

### Namespace and Aliasing:

When you import a module or package, you can access its attributes using dot notation. You can also **use the as keyword to provide an alias for the imported module or package.**

Example:
```python
# Importing with an alias
import my_module as mm

result = mm.greet("Bob")

print(result)
# Output: Hello, Bob!
```

```python
# Importing specific functions with aliases
from my_module import greet as custom_greet

result = custom_greet("Charlie")

print(result)
# Output: Hello, Charlie!
```