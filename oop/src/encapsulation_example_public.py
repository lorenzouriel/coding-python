class MyClass:
    def __init__(self): # Default Constructor
        self.public_attribute = 10

    def public_method(self):
        return "This is a public method"

obj = MyClass()
print(obj.public_attribute)  # Output: 10
print(obj.public_method())   # Output: This is a public method