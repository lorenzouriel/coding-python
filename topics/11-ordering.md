# Ordering
Every list has a Sort method that sorts its space. **If you don't want to mess up your list, you can use `Sorted`**
```python
x = [4, 1, 2, 3]

y = sorted(x) # y is [1, 2, 3, 4]
x.sort() # x is [1, 2, 3, 4]
```

Sort and Sorted organize the list in ascending order, if you want descending order use the parameter: `reverse = True`
```python
y = sorted(x, reverse = True) # y is [4, 3, 2, 1]
```