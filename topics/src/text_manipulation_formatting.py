name = "Alice"
age = 25

# Using % operator
message = "My name is %s and I am %d years old" % (name, age)
print(message)

# Using format() method
message = "My name is {} and I am {} years old".format(name, age)
print(message)

# Using f
print(f"My name is {name} and my age is {age}")