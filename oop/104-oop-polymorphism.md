# Polymorphism
Is a fundamental concept in object-oriented programming (OOP) that **allows objects of different classes to be treated as objects of a common superclass.** It enables code to **work with objects of multiple types through a uniform interface, making the code more flexible and reusable.**

**Method Overriding (Runtime Polymorphism):** Method overriding **occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.** 
- *This allows objects of different classes to **invoke the same method name but execute different implementations based on their respective classes.***

**Example:**
```python
class Animal:
    def make_sound(self):
        print("Animal makes a generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

# Create instances of different subclasses
animal = Animal()
dog = Dog()
cat = Cat()

# Call the make_sound method on each object
animal.make_sound()  # Output: Animal makes a generic sound
dog.make_sound()     # Output: Dog barks
cat.make_sound()     # Output: Cat meows
```

**In this example:**
- The `Animal` class defines a method `make_sound()` with a generic implementation.
- The `Dog` and `Cat` classes **override** the `make_sound()` method with their own specific implementations.
- Despite all objects being called using the same method name (`make_sound()`), each object **executes its respective implementation based on its class, *demonstrating polymorphic behavior.***

Polymorphism allows you to write code that can **operate on objects of different classes in a uniform manner, promoting code reuse, flexibility, and extensibility.**


### Polymorphism vs. Inheritance
Polymorphism and inheritance are both fundamental concepts in object-oriented programming (OOP), but they serve different purposes and address different aspects of software design:

**1. Inheritance:**
- **Definition:** Inheritance is a **mechanism by which a new `class` (`subclass` or `derived class`) is created from an existing `class` (`superclass` or `base class`), inheriting its `attributes` and `methods`.**
    - ***The subclass can then extend or modify the behavior of the superclass by adding new attributes or methods, or by overriding existing ones.***


**2. Polymorphism:**
- **Definition:** Polymorphism is the **ability of objects of different classes to be treated as objects of a common superclass.** It allows methods to be **invoked on objects of different types through a uniform interface, with the actual method implementation determined at runtime based on the object's class.**


In summary, **inheritance focuses on the hierarchical organization and sharing of code between classes**, while **polymorphism emphasizes the flexibility and uniform treatment of objects of different types through a common interface.** 

While they are related concepts and often used together in object-oriented design, they address different aspects of object-oriented programming.