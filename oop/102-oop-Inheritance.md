# Inheritance
It is a mechanism that **allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class.** Inheritance is the capability of one class to **derive or inherit the properties from another class.**

**Benefits of inheritance are:**
- *Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class.*
- It represents real-world relationships well.
- It provides the reusability of a code.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
- Inheritance offers a simple, understandable model structure. 
- Less development and maintenance expenses result from an inheritance. 

**Here's an example demonstrating inheritance in Python:**
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    # Method speak from the class Animal
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass 1
class Dog(Animal):
    # Inherit Method Speak from parent class (Animal)
    def speak(self):
        return f"{self.name} says Woof!"

# Subclass 2
class Cat(Animal):
    # Inherit Method Speak from parent class (Animal) 
    def speak(self):
        return f"{self.name} says Meow!"

# Creating objects of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

### Polymorphism vs. Inheritance
Polymorphism and inheritance are both fundamental concepts in object-oriented programming (OOP), but they serve different purposes and address different aspects of software design:

**1. Inheritance:**
- **Definition:** Inheritance is a **mechanism by which a new `class` (`subclass` or `derived class`) is created from an existing `class` (`superclass` or `base class`), inheriting its `attributes` and `methods`.**
    - ***The subclass can then extend or modify the behavior of the superclass by adding new attributes or methods, or by overriding existing ones.***


**2. Polymorphism:**
- **Definition:** Polymorphism is the **ability of objects of different classes to be treated as objects of a common superclass.** It allows methods to be **invoked on objects of different types through a uniform interface, with the actual method implementation determined at runtime based on the object's class.**


In summary, **inheritance focuses on the hierarchical organization and sharing of code between classes**, while **polymorphism emphasizes the flexibility and uniform treatment of objects of different types through a common interface.** 

They are related concepts and often used together in object-oriented design, they address different aspects of object-oriented programming.