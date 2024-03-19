class MyClass:
    def __init__(self):
        self._protected_attribute = 30

    def _protected_method(self):
        return "This is a protected method"

obj = MyClass()
print(obj._protected_attribute)   # Output: 30
print(obj._protected_method())    # Output: This is a protected method