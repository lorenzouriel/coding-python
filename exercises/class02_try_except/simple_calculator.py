# Develop a simple calculator that accepts two numeric inputs and an operator (+, -, *, /) from the user. 
# Use try-except to handle division by zero and non-numeric input. 
# Use if-elif-else to perform mathematical operation based on the given operator. Print the result or an appropriate error message.

try:
    num1 = float(input("Tip the first number: "))
    num2 = float(input("Tip the second number: "))
    operator = input("Tip the operator operador (+, -, *, /): ")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/' and num2 != 0:
        result = num1 / num2
    else:
        print("Invalid operator or Zero Division is not possible.")
    print("Resultado:", result)
except ValueError:
    print("Error: Invalid input. Check if you insert the right numbers")