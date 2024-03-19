# A TypeError occurs in Python when an operation or function is applied to an object of inappropriate type. Python doesn't know how to apply the operation because the data types are not compatible.
try:
    resultado = len(5)
except TypeError as e:
    print(e)

# The code above tries to get the length of an integer, which doesn't make sense, resulting in the error message: "object of type 'int' has no len()".