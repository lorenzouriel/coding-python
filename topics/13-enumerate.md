# Enumerate
The `enumerate()` function in Python is a `<built-in>` function that **allows you to iterate over a sequence (like a list, tuple, or string) while keeping track of the index and the corresponding element.** It returns pairs of index and item as tuples.

**Here's the basic syntax:**
```python
enumerate(iterable, start=0)
```
- `iterable`: The iterable you want to enumerate.
- `start` (optional): The index at which to start counting. The default is 0.

**Here's an example of using `enumerate()`:**
```python
my_list = ['apple', 'banana', 'cherry']

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
```

*Output:*
```python
Index: 0, Value: apple
Index: 1, Value: banana
Index: 2, Value: cherry
```

**You can also specify a `start` value for the index:**
```python
for index, value in enumerate(my_list, start=1):
    print(f"Index: {index}, Value: {value}")
```