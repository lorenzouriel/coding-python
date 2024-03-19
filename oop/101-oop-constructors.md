# Constructors
Constructors are generally used for instantiating an object.  

The task of constructors is to **initialize(assign values)** to the data members of the class when an object of the class is created. In Python the `__init__()` method is called the constructor and is always called when an object is created.

**1. Default Constructor:** The default constructor is a constructor that doesn't accept any arguments other than `self`, which is a reference to the instance being constructed. **It initializes the object's attributes to default values, or it can perform other initialization tasks required for the object.**
```python
class Person:
    def __init__(self):
        # Default constructor initializes attributes with default values
        self.name = "John Doe"
        self.age = 0

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Default constructor
person = Person()  
person.display_info()  
```

**2. Parameterized Constructor:** A parameterized constructor is a constructor that accepts additional parameters besides `self`. **These parameters are provided by the programmer and are used to initialize the object's attributes based on the values passed during object creation.**

Here's an example demonstrating both types of constructors:
```python
class Employee:
    def __init__(self, name, emp_id):
        # Parameterized constructor initializes attributes with provided values
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.emp_id}")

# Parameterized constructor
employee = Employee("Alice", 1001)  

employee.display_info()
```