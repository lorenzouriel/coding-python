# Tuples, Lists and Dictionaries
Tuples, lists, and dictionaries are three different data structures in Python, each serving different purposes. 

**1. Tuples:**
A tuple is an ordered and immutable collection of elements. Once a tuple is created, you cannot modify its contents.

Tuples are defined using parentheses `()`.

- Example:
```python
# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements
print(my_tuple[0])     # Output: 1
print(my_tuple[3])     # Output: apple


# Tuple unpacking
a, b, c, fruit1, fruit2 = my_tuple
print(a, b, c)         # Output: 1 2 3
print(fruit1, fruit2)  # Output: apple banana
```


**2. Lists:**
A list is an ordered and mutable collection of elements. 

Lists are defined using brackets `[]`.

- Example:
```python
# Creating a list
my_list = [1, 2, 3, "apple", "banana"]

# Accessing elements
print(my_list[0])      # Output: 1
print(my_list[3])      # Output: apple

# Modifying elements
my_list[0] = 100

# Adding elements
my_list.append("orange")
my_list.insert(0, "kiwi") # Position, Value

# Copy list
list1 = my_list[:]  # Copy the content of my_list into list1

# Remove elements
del list1[3]  # Remove element at index 3
list1.pop(3)  # Remove and return element at index 3

# Remove 'apple' from my_list
my_list.remove('apple')  # Remove the first occurrence of 'apple' from the list
list1.remove('banana')  # Remove the first occurrence of 'apple' from the list


# Print the updated lists
print("Updated list1:", list1) # Output: Updated list1: ['kiwi', 100, 2, 'orange']
print("Updated my_list:", my_list) # Updated my_list: ['kiwi', 100, 2, 3, 'banana', 'orange']
```


**3. Dictionaries:**
A dictionary is an unordered collection of key-value pairs. Each key must be unique, and you can use it to access its associated value.

Dictionary are defined using brackets `{}`.

Example:
```python
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
```

### When to use?
- *Use Tuples when:*
	- You want an ordered and immutable collection.
	- The data should not be modified throughout the program.
	- Parentheses `()` -> `Value`

- *Use Lists when:*
	- You want an ordered and mutable collection.
	- You need to modify, add, or remove elements.
	- Brackets `[]` -> `Index and Value`

- *Use Dictionaries when:*
	- You need to store data in key-value pairs.
	- You want a fast way to look up values based on keys.
	- Keys `{}` -> `Key and Value`