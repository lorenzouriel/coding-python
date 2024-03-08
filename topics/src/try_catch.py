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