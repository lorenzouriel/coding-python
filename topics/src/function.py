# Defining a Function
def greet(name):
    """This function prints a greeting."""
    print(f"Hello, {name}!")

greet("Lorenzo")
# Output: Hello, Lorenzo!


# Returning Values
def add(x, y):
    """This function returns the sum of two numbers."""
    return x + y

result = add(3, 5)
print(result)


# Default Parameters
def power(base, exponent=2):
    """This function calculates the power of a number with a default exponent of 2."""
    return base ** exponent

print(power(3))
# Output: 9

print(power(3, 3))
# Output: 27


# Optional Parameters
def my_sum(a, b, c=0):
    """This function calculates the power of a number with a optional parameter in C""" 
    sum = a + b + c
    return sum
 
print(my_sum(4, 5)) 
# Output: 9


# Keyword Arguments
def person_info(**kwargs):
    """This function prints information about a person."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="John", age=30, city="New York")
# Output:
# name: John
# age: 30
# city: New York


# Variable Number of Arguments
def average(*numbers):
    """This function calculates the average of a variable number of arguments."""
    return sum(numbers) / len(numbers)

print(average(1, 2, 3, 4, 5))
# Output: 3.0