# Defining Functions
# To create a function in Python, you use the `def` keyword, followed by a `function name`, parentheses () containing zero or more "parameters", and a colon:. The indented block of code that follows is the body of the function.
def minha_funcao():
    return "Hello, World!"

# Function Names
# Function names follow the same rules as variable names in Python: they can contain letters, numbers (not as the first character) and underscores (_), but not spaces or special characters. Function names must be descriptive and, by convention, use snake_case.

# Parameters and Arguments
# -- Parameters are the variables listed in parentheses in the function definition. They are like placeholders for the data that the function will process.
# -- Arguments are the actual values ​​passed to the function when it is called.
def soma(a, b):
    return a + b

# Important keywords
# -- def starts the definition of a function.
# -- return is used to return a value from the function. If omitted, the function returns None by default.
# -- pass can be used as a placeholder for an empty function, meaning "nothing".

# Calling Functions
# To call a function, use the function name followed by parentheses containing the required arguments.
resultado = soma(5, 3)
print(resultado)  # Saída: 8

# Default Values ​​and Named Arguments
# Functions can have parameters with default values, allowing them to be called with fewer arguments.
def cumprimentar(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

# Você também pode chamar funções com argumentos nomeados para maior clareza.
cumprimentar(mensagem="Bem-vindo", nome="João")