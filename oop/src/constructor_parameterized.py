class Employee:
    def __init__(self, name, emp_id):
        # Parameterized constructor initializes attributes with provided values
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.emp_id}")

# Parameterized constructor
employee = Employee("Alice", 1001)  

employee.display_info()