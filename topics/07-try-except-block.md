# Try-Except Block
A try-except block is **used for exception handling.** 

It allows you to catch and handle exceptions that might occur during the execution of your code. Here's a simple example:
```python
try:
    # Code that might raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    result = num1 / num2

    # This will not be executed if a division by zero occurs
    print(f"The result of the division is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("This block will be executed no matter what.")
```

In this example:
- The `try` block contains the code that might raise an exception.
- The `except` blocks catch specific types of exceptions and handle them. The `except Exception as e` block catches any other exceptions.
- The `finally` block contains code that will be executed no matter what, whether an exception occurred or not.

You can tailor the except blocks to handle specific exceptions relevant to your code. 

Using `except Exception as e` is a catch-all that can be helpful for debugging but should be used carefully in production code.