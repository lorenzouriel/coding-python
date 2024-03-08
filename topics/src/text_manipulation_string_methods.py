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