# Initialize variables for loop control
name_valid = False
salary_valid = False
bonus_valid = False

# Loop to check the name
while not name_valid:
    try:
        name = input("Enter your name: ")
        if len(name) == 0:
            raise ValueError("Name cannot be empty.")
        elif any(char.isdigit() for char in name):
            raise ValueError("Name should not contain numbers.")
        else:
            print("Valid name:", name)
            name_valid = True
    except ValueError as e:
        print(e)

# Loop to check the salary
while not salary_valid:
    try:
        salary = float(input("Enter your salary: "))
        if salary < 0:
            print("Please enter a positive value for the salary.")
        else:
            salary_valid = True
    except ValueError:
        print("Invalid input for salary. Please enter a number.")

# Loop to check the bonus
while not bonus_valid:
    try:
        bonus = float(input("Enter the bonus amount received: "))
        if bonus < 0:
            print("Please enter a positive value for the bonus.")
        else:
            bonus_valid = True
    except ValueError:
        print("Invalid input for bonus. Please enter a number.")

received_bonus = 1000 + salary * bonus  # Simple example of bonus calculation

# Print information for the user
print(f"{name}, your salary is ${salary:.2f} and your final bonus is ${received_bonus:.2f}.")