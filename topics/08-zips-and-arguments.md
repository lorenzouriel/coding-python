# Zip and Arguments
In Python, the `zip()` function is **used to combine multiple iterables (such as lists or tuples) into an iterator of tuples.** It takes in multiple iterables and returns an iterator that produces tuples containing elements from the input iterables.

**1. Zip:**
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
 
# Using zip to combine two lists
zip(list1, list2)
zipped = zip(list1, list2)

# Converting the zip object to a list of tuples
result = list(zipped)
print(result)
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

**2. Unzipping:** You can use the `*` (unpacking) operator to unzip the zipped result:
```python
unzipped = list(zip(*result))

print(unzipped)
# Output: [(1, 2, 3), ('a', 'b', 'c')]
```

**3. Zip with Arguments:** You can use `zip()` with more than two iterables, and even with different types of iterables:
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
tuple1 = ('x', 'y', 'z')

zipped = zip(list1, list2, tuple1)

result = list(zipped)
print(result)
# Output: [(1, 2), ('a', 'b'), ('x', 'y')]
```

**4. Unzipping with Arguments:** Similarly, you can use the `*` operator to unzip with more than two iterables:
```python
unzipped = list(zip(*result))

print(unzipped)
# Output: [(1, 2), ('a', 'b'), ('x', 'y')]
```

Using `zip()` and unpacking is a convenient way to work with multiple iterables simultaneously.

Keep in mind that the length of the resulting iterable is determined by the shortest input iterable, so elements from longer iterables beyond the length of the shortest iterable are ignored.

Here's an example using `zip()` to illustrate this concept:
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
list3 = ['x', 'y']

result = zip(list1, list2, list3)
print(list(result))  # Output: [(1, 'a', 'x'), (2, 'b', 'y')]
```
In this example:
- `list1` has 3 elements.
- `list2` has 4 elements.
- `list3` has 2 elements.

Since `list3` is the shortest iterable, the resulting iterable from `zip()` contains only 2 tuples, each containing elements from `list1`, `list2`, and `list3` respectively. The fourth element from `list2` is ignored because there is no corresponding element in `list3`.

We lead with this example in the code `src/zip.py`