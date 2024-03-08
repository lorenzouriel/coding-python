# Text Manipulation
Text manipulation in Python involves working with strings and performing various operations such as string concatenation, slicing, searching, and formatting. 

Here are some basic text manipulation operations in Python:

**1. String Concatenation:**
You can concatenate (combine) two or more strings using the + operator:
```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World
```

**2. String Slicing:**
You can extract a portion of a string using slicing:
```python
text = "Python is awesome"
substring = text[7:11]
print(substring)  # Output: is

[Start : End : Jump]
```

**3. String Methods:**
Python provides various built-in methods for string manipulation, such as `upper()`, `lower()`, `replace()`, `split()`, and more:
```python
text = "Python programming"

# Converting to uppercase
upper_text = text.upper()  # Output: PYTHON PROGRAMMING
print(upper_text)     # Output: PYTHON PROGRAMMING


# Converting to lowercase
lower_text = text.lower()  # Output: python programming
print(lower_text)     # Output: python programming


# Replacing "python" with "Java" (case-sensitive)
replace_text = text.replace("Python", "Java")  # Output: Java Programming
print(replace_text)   # Output: Java programming


# Splitting the string into a list of words
split_text = text.split()  # Output: ['Python', 'Programming']
print(split_text)     # Output: ['python', 'programming']


# Capitalizing the first letter of the string
capitalize = text.capitalize()  # Output: Python programming
print(capitalize)


# Converting the string to title case
title = text.title()  # Output: Python Programming
print(title)


# Stripping leading and trailing whitespace
strip = text.strip()  # Output: "Python Programming" (no space)
strip_right = text.rstrip()  # Output: "Python Programming" (no right space)
strip_left = text.lstrip()  # Output: "Python Programming" (no left space)
print(strip)


# Join the spaces
join = '-'.join(text) # Output is "python-programming"
print(join)
```

**4. String Formatting:**
You can format strings using the `%` operator or the `format()` method:
```python
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
```

**5. String Analysis:**
```python
# You can check if a substring exists in a string using the in keyword
text = "Python is easy to learn"

contains_python = "Python" in text
print(contains_python)  # Output: True

print(len(text)) # 23

print(text.count('y')) # 1

print(text.find('Python')) # Where starts (0) position
```