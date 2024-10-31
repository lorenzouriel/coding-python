# SOLID Principles

The **SOLID principles—guidelines** for writing maintainable, scalable, and robust code—can be applied in Python to help improve the structure and clarity of code. Here’s how each principle can be implemented in Python:

### 1. Single Responsibility Principle (SRP)
- **Definition:** A class should have one, and only one, reason to change.
- **Python Example:**
```python
class FileHandler:
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

class TextProcessor:
    def process_text(self, text):
        return text.upper()
```

- **Explanation:** Each class has a single responsibility: `FileHandler` handles file operations, and `TextProcessor` processes text.

### 2. Open/Closed Principle (OCP)
- **Definition:** Software entities should be open for extension but closed for modification.
- **Python Example:**
```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):
        return price - self.amount
```

- **Explanation:** New discount strategies can be added by extending `DiscountStrategy` without modifying existing code.

### 3. Liskov Substitution Principle (LSP)
- **Definition:** Subtypes should be substitutable for their base types without altering the correctness of the program.
- **Python Example:**
```python
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich cannot fly")
```

- **Explanation:** In this example, `Ostrich` should not inherit `Bird` if it cannot fly, as it violates LSP. A better solution could be to separate the `Flyable` behavior into its own class.

### 4. Interface Segregation Principle (ISP)
- **Definition:** Clients should not be forced to depend on interfaces they do not use.
- **Python Example:**
```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        print("Worker is working")

    def eat(self):
        print("Worker is eating")

class Robot(Workable):
    def work(self):
        print("Robot is working")
```

- **Explanation:** By separating interfaces, `Robot` isn’t forced to implement the `eat` method.

### 5. Dependency Inversion Principle (DIP)
- **Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions.
- **Python Example:**
```python
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Sending email with message: {message}")

class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)
```

- **Explanation:** `NotificationService` depends on an abstraction (`NotificationSender`), allowing it to work with any notification method (email, SMS, etc.) by injecting the appropriate sender at runtime.

### Benefits of Applying SOLID Principles in Python
- **Readability:** Improves code readability and intent.
- **Flexibility:** Makes the code easier to extend without modifying existing code.
- **Reusability:** Components are loosely coupled and more modular.
- **Maintainability:** Reduces the risk of introducing bugs when requirements change.

Using these principles makes Python code more structured and ready for scaling or future updates, enhancing the codebase's overall quality.