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