# Ask user his name
try: 
    name = input("Tip your name: ")

    # Check if the name is empty
    if len(name) == 0:
        raise ValueError("The name can´t be empty")
    # Check numbers in the name
    elif any(char.isdigit() for char in name):
        raise ValueError("The name can´t contain numbers")
    else:
        print("Valid name:", name)
except ValueError as e:
    print(e)


# Ask user to digit your current salary and convert to float
try: 
    salary = float(input("Tip your current salary: R$ "))
    if salary < 0:
        print("WTF! You can't work for free. Tip a positive salary")
except ValueError: 
    print("Wrong input number. Please, digite your corrected currnt salary: ")


# Ask user to input the bonus value and convert to float
try:
    received_bonus = float(input("Tip the value of your received bonus: "))
    if received_bonus < 0:
        print("Tip a positive bonus or ask your boss: WHAT TYPE OF BONUS IS THIS?")
except ValueError:
    print("The input bonus is not write. Please, tip a number: ")


# Final logic to calculate bonus
final_bonus = received_bonus * 1.2
kpi = (salary + final_bonus) / 1000

# Print values
print(f"Your KPI is: {kpi:.2f}")
print(f"{name}, your salary is R${salary:.2f} and your final bonus is R${final_bonus:.2f}.")