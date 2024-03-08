# Iterate over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# Exit the loop when the value is 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# Using else with a for loop
for i in range(5):
    print(i)
else:
    print("Loop completed")
