# The try-except structure is used for exception handling in Python. An exception is an error that occurs during program execution and that, if not handled, interrupts the normal flow of the program and ends its execution.

# Example
try: 
    result = 10 / 0
except ZeroDivisionError:
    print("Zero division is not possible")