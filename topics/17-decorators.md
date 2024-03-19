# Decorators
Decorators in Python **provide a way to modify or extend the behavior of functions or methods without changing their source code.** 

They allow you to wrap another function and add additional functionality to it.

Decorators are especially **useful for implementing cross-cutting concerns such as logging, caching, authentication, and more.**

### Here's how decorators work:

**1. `Decorator Function`:** A decorator is itself a **function that takes another function as an argument.**

**2. `Wrapper Function`:** Inside the decorator function, a new function (usually called a `"wrapper"` function) is defined. This wrapper function **typically adds some extra functionality before and/or after calling the original function.**

**3. `Returning the Wrapper`:** The decorator function **returns the wrapper function**, effectively **replacing the original function with the wrapped version.**

**4. `Using the Decorator`:** To apply a decorator to a function, you use the **`@decorator_name` syntax above the function definition.** This tells Python to **automatically pass the function to the decorator and replace it with the wrapped version.**

### Now, let's see an example:

Suppose you want to log the arguments and return values of a function. You can create a decorator for this purpose:
```python
def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_arguments_and_result
def add(x, y):
    return x + y

result = add(3, 5)
print(f"Result of add function: {result}")
```

In this example:

- `log_arguments_and_result` is the decorator function. It takes another function (`func`) as an argument.
- Inside the decorator function, there's a wrapper function (`wrapper`) that logs the arguments passed to `func`, then calls `func` with those arguments, logs the return value, and finally returns the result.
- The `@log_arguments_and_result` syntax applies the decorator to the add function, replacing it with the wrapped version.
- When you call add(`3, 5`), the `wrapper` function is invoked instead. It logs the arguments `3` and `5`, calls the original add function, logs the result `8`, and returns it.

The final output will be:
```
Calling add with arguments: args=(3, 5), kwargs={}
add returned: 8
Result of add function: 8
```

This demonstrates how decorators can be used to add logging functionality to a function without modifying its original code.


### Another Example
- ***And more simple too***

Here's a simpler example of a decorator that prints a message before and after calling a function:
```python
def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

In this example:

- `my_decorator` is the decorator function that takes another function (`func`) as its argument.
- Inside `my_decorator`, there's a wrapper function (`wrapper`) that prints a message before and after calling the original function `func`.
- The `@my_decorator` syntax is used to apply the `my_decorator` decorator to the `say_hello()` function.
- When `say_hello()` is called, it actually invokes the `wrapper` function created by the `decorator`. As a result, "Before calling the function" is printed, followed by "Hello!" (the output of `func()`), and then "After calling the function".