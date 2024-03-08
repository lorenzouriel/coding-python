# Creating a dictionary
my_dict = dict() 
my_dict = {"name": "John", "age": 25, "city": "New York"} # Key-Value Pair

# Accessing values
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 25

print(my_dict.values()) # Only Values
print(my_dict.keys())   # Only Keys
print(my_dict.items())  # Keys and Values

# Modifying values
my_dict["age"] = 26

# Adding values/keys 
my_dict["occupation"] = "Engineer"
print(f"My updated dictionary: {my_dict}") # {'name': 'John', 'age': 26, 'city': 'New York', 'occupation': 'Engineer'}


# Removing 
del my_dict ["occupation"]
print(f"My updated dictionary: {my_dict}") # {'name': 'John', 'age': 26, 'city': 'New York'}

my_dict.pop("age")
print(f"My updated dictionary: {my_dict}") # {'name': 'John', 'city': 'New York'}

my_dict.clear() # Clean all the dict