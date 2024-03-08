# Conditions
In Python, conditional statements allow you to make decisions in your code based on certain conditions. The primary constructs for implementing conditions are if, elif (short for "else if"), and else. Here's an overview of how you can use them:

**1. if Statement:**
The if statement allows you to execute a block of code if a certain condition is true.
```python
x = 10

if x > 5:
    print("x is greater than 5")
```

**2. if-else Statement:**
The if-else statement lets you specify two blocks of code: one to be executed if the condition is true, and another if it's false.
```python
y = 3

if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")
```

**3. if-elif-else Statement:**
The if-elif-else statement allows you to check multiple conditions in sequence. If the first condition is true, the corresponding block of code is executed, and the rest of the conditions are skipped. If none of the conditions is true, the else block (if present) is executed.

```python
grade = 75

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

**Example with User Input:**
```python
# Get user input
user_input = int(input("Enter a number: "))

# Check the condition
if user_input > 0:
    print("The number is positive.")
elif user_input < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

These are basic examples of how to use conditional statements in Python. Conditions are often expressed using ***comparison operators*** (`==`, `!=`, `<`, `>`, `<=`, `>=`) or ***logical operators*** (`and`, `or`, `not`). You can also nest conditional statements to handle more complex scenarios.