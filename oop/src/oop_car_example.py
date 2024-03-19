class Car:
    def __init__(self, make, model, year):
        # Attributtes
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False # Addittional Attribute
    
    # Methods
    def start_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine is now running")

    def stop_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine is now stopped")

    def honk(self):
        print(f"{self.year} {self.make} {self.model} says honk! Honk!")


# Creating objects (instances) of the Car Class
car1 = Car("Toyota", "Camry", 2022) 
car2 = Car("Honda", "Accord", 2023)

# Accessing attributes 
print(f"Car 1: {car1.year} {car1.make} {car1.model}") 
print(f"Car 2: {car2.year} {car2.make} {car2.model}")

# Calling methods 
car1.start_engine() 
car2.start_engine()

# Honking the horns 
car1.honk()
car2.honk()

# Stopping the engines 
car1.stop_engine() 
car2.stop_engine()