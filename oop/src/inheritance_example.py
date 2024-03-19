# Parent class
class Animal:
    def __init__(self, name): # Paraterized constructor
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
    
# Subclass 3
class Chicken(Animal):
    # Inherit Method Speak from parent class (Animal) 
    def speak(self):
        return f"{self.name} says cocorico!"
    
# Creating objetcs of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskas")
chicken = Chicken("Gus Fring")

# Calling Methods
print(dog.speak())
print(cat.speak())
print(chicken.speak())