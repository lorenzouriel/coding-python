# Write a program that converts temperature from Celsius to Fahrenheit. 
# The program must ask the user for the temperature in Celsius and, using try-except, ensure that the input is numeric, handling any ValueError. 
# Print the result in Fahrenheit or an error message if the input is not valid.

try:
    celsius = float(input("Tip the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
except ValueError:
    print("Please, tip a valid number for temperature")