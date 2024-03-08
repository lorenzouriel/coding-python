# List Comprehension
List comprehension **is a concise way to create lists in Python.** It allows you to construct a list by specifying the elements you want to include, **using a single line of code.** The basic syntax of a list comprehension is:
```python
new_list = [expression for item in iterable if condition]
```
- `expression:` The expression to be evaluated for each element.
- `item:` The variable representing an element from the iterable.
- `iterable:` The iterable (e.g., a list, tuple, or string) you are iterating over.
- `condition` (optional): An optional condition that filters the elements.


### Let´s compare some examples:

- **Example 1:** Squaring Numbers
```python
# Using a for loop
squares = []
for i in range(5):
    squares.append(i ** 2)

# Using list comprehension
squares_lc = [x ** 2 for x in range(5)]

print(squares)    # Output: [0, 1, 4, 9, 16]
print(squares_lc) # Output: [0, 1, 4, 9, 16]
```


- **Example 2:** Filtering Odd Numbers
```python
# Using a for loop
odd_numbers = []
for i in range(10):
    if i % 2 != 0:
        odd_numbers.append(i)


# Using list comprehension
odd_numbers_lc = [x for x in range(10) if x % 2 != 0]

print(odd_numbers)    # Output: [1, 3, 5, 7, 9]
print(odd_numbers_lc) # Output: [1, 3, 5, 7, 9]
```


- **Example 3:** Creating a List of Strings
```python
words = ['hello', 'world', 'python']

# Using a for loop
upper_words = []
for word in words:
    upper_words.append(word.upper())

# Using list comprehension
upper_words_lc = [word.upper() for word in words]

print(upper_words)    # Output: ['HELLO', 'WORLD', 'PYTHON']
print(upper_words_lc) # Output: ['HELLO', 'WORLD', 'PYTHON']
```

- **Example 4:** Extracting Even Numbers from a Tuple
```python
tuple_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Using a for loop
even_numbers = []
for num in tuple_numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# Using list comprehension
even_numbers_lc = [num for num in tuple_numbers if num % 2 == 0]

print(even_numbers)    # Output: [2, 4, 6, 8, 10]
print(even_numbers_lc) # Output: [2, 4, 6, 8, 10]
```