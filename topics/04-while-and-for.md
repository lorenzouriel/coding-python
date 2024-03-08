# While and For
In Python, both for and while are loop structures that allow you to repeatedly execute a block of code. They serve different use cases, and I'll explain each one.

**1. for Loop:**
The for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

- Syntax:
```python
for variable in sequence(start, end, step): 
    # Code to be executed in each iteration
```

- Example:
```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**2. while Loop:**
The while loop is used to repeatedly execute a block of code as long as the specified condition is true.

- Syntax:
```python
while condition:
    # Code to be executed as long as the condition is true
```

- Example:
```python
# Print numbers from 1 to 5 using a while loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1
```

**3. break and continue Statements:**
The break statement is used to exit the loop prematurely.
```python
# Exit the loop when the value is 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

- The continue statement is used to skip the rest of the code inside the loop for the current iteration and jump to the next iteration.
```python
# Skip printing even numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)
```

**4. else Clause with Loops:**
Both for and while loops can have an optional else clause that is executed when the loop condition becomes false or when the loop completes its iterations.

- Example:
```python
# Using else with a for loop
for i in range(5):
    print(i)
else:
    print("Loop completed")

    
# Using else with a while loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1
else:
    print("Loop completed")
```