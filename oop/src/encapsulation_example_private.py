class MyClass:
    def __init__(self):
        self.__private_attribute = 20

    def __private_method(self):
        return "This is a private method"

obj = MyClass()
# Attempting to access private attribute/method directly will raise an AttributeError
print(obj.__private_attribute)
print(obj.__private_method())
# AttributeError: 'MyClass' object has no attribute '__private_attribute'. Did you mean: '_MyClass__private_attribute'?