# Type checking is the process of checking the type of a variable. This can be useful to ensure that operations or functions are only applied to supported data types, avoiding run-time errors.

# To check the type of a variable in Python, you can use the type() or isinstance() function.

number = 10
if isinstance(number, int):
    print("The variable is an integer")
else:
    print("The variables is not an integer")