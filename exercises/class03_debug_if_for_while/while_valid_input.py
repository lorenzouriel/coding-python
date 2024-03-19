number = int(input("Tip a number 01 to 10: "))
while number < 1 or number > 10:
    print("Number out of the interval!")
    number = int(input("Please, tip a number 01 to 10: "))

print("Valid Number!")