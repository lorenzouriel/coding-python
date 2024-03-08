# Set ()
Set is an **unordered collection of unique elements.** 

The elements in a set must be hashable, meaning they can be converted to a hash value, and they must be immutable. 

Sets are defined using curly braces `{}` or the `set()` constructor.

**1. Creating a Set:**
```python
my_set = {1, 2, 3, 4, 5}

my_set = set()
```

**2. Adding and Removing Elements:**
```python
# Adding an element
my_set.add(6)

# Removing an element
my_set.remove(3)
```

**3. Set Operations:**
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)  # or use the pipe operator: union_set = set1 | set2

# Intersection
intersection_set = set1.intersection(set2)  # or use the ampersand operator: intersection_set = set1 & set2

# Difference
difference_set = set1.difference(set2)  # or use the minus operator: difference_set = set1 - set2
```

**4. Checking Membership:**
```python
# Checking membership
result = 3 in my_set
print(result)  # Output: False
```

**5. Iterating Through a Set:**
```python
# Iterating through a set
for element in my_set:
    print(element)
```