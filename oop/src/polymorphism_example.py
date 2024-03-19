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