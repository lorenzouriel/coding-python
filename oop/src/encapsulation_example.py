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