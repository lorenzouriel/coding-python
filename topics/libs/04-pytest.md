# Pytest
Pytest is a Python testing framework that makes it easy to write and run automated tests. It is widely used in the Python community for testing software applications and libraries. Pytest offers a simple and intuitive approach to writing tests, allowing developers to focus more on the test logic itself and less on the structure of the test code.

## Documentation
You can find the full documentation [here](https://pytest.org/en/7.4.x/contents.html)

## Types of Tests (an Overview)
**1. Unit Tests**
- Test a "unit" of code in isolation (such as functions or methods) to ensure it is working as expected

**2. Integration Tests**
- They test the integration between different parts of the code (for example, the extract modules check if it can access AWS). It aims to detect possible failures in the interaction between different modules.

**3. Functional Tests**
- Confirm that the entire project is working as it should in the full scenario.

## Main commands
- Runs all tests in the current directory and subdirectories
```py
pytest
```

- Runs all tests contained in the specified file.
```py
pytest [filename]
```

- Enables verbose output, providing more details about the tests being run.
```py
pytest -v
```

- Generates a test report in an HTML file, requires the pytest-html plugin.
```py
pytest --html=report.html
```

- Generates a code coverage report when used with the pytest-cov plugin.
```py
pytest --cov=[directory]
```