# Encapsulation
Involves agroup data (attributes) and methods (functions) that operate on that data within a single unit, known as a class. It **allows you to control access to the internal state of an object, ensuring that the object's data is accessed and modified only through well-defined interfaces (methods), while hiding the internal implementation details.**

**Here are the key aspects of encapsulation:**
- **Data Hiding:** Encapsulation hides the internal state of an object from external code.
- **Access Control:** Encapsulation provides control over how data is accessed and modified.
- **Information Abstraction:** Encapsulation allows you to abstract the implementation details of a class, exposing only the essential functionality to the outside world.
- **Flexibility and Maintainability:** Encapsulation promotes modularity by encapsulating related data and behavior within a single unit (class).

**Example of encapsulation in Python:**
```python
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def get_make(self):
        return self.__make  # Getter method  

    def set_make(self, make):
        self.__make = make  # Setter method
    
    def get_model(self):
        return self.__model  # Getter method

    def set_model(self, model):
        self.__model = model  # Setter method

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Accessing and modifying private attributes using getter and setter methods
print(my_car.get_make())  # Output: Toyota
print(my_car.get_model())  # Output: Corolla

# Acessing the setter methods
my_car.set_make("Honda")
my_car.set_model("Fit")

print(my_car.get_make())  # Output: Honda
print(my_car.get_model())  # Output: Fit
```

**In this example:**
- The `Car` class encapsulates the `make` and `model` of a car as private attributes (`__make` and `_model`).
- `Getter` and `setter` methods (`get_make()`, `set_make()`, `get_model()`, `set_model()`) provide controlled access to these private attributes, **allowing external code to retrieve and modify them.**
- External code interacts with the `Car` object **through the public interface provided by the getter and setter methods**, ensuring data integrity and abstraction of internal implementation details.


### The public, private and protected exists in Python?
- *Yes, but it's different!*

**1. Public:** All attributes and methods are public by default, meaning **they can be accessed and modified from outside the class.**

**2. Private:** Attributes and methods **that are intended to be private are prefixed with double underscores (`__`).** This doesn't make them truly private, but it mangles their names, making them harder to access directly from outside the class.*

**3. Protected:** Attributes and methods **that are intended to be protected are prefixed with a single underscore (`_`).** This doesn't enforce any access control, but it *serves as a visual indicator to indicate that the attribute or method is intended for internal use or for subclasses.*

**Conventions Examples:**
- **Public**
```python
class MyClass:
    def __init__(self): # Default Constructor
        self.public_attribute = 10

    def public_method(self):
        return "This is a public method"

obj = MyClass()
print(obj.public_attribute)  # Output: 10
print(obj.public_method())   # Output: This is a public method
```

- **Private**
```python
class MyClass:
    def __init__(self):
        self.__private_attribute = 20

    def __private_method(self):
        return "This is a private method"

obj = MyClass()
# Attempting to access private attribute/method directly will raise an AttributeError
# print(obj.__private_attribute)
# print(obj.__private_method())

# AttributeError: 'MyClass' object has no attribute '__private_attribute'. Did you mean: '_MyClass__private_attribute'?
```

- **Protected**
```python
class MyClass:
    def __init__(self):
        self._protected_attribute = 30

    def _protected_method(self):
        return "This is a protected method"

obj = MyClass()
print(obj._protected_attribute)   # Output: 30
print(obj._protected_method())    # Output: This is a protected method
```