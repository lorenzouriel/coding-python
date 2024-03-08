# ANSI escape codes for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
EXAMPLE = "\033[4;31;47m"

# Example usage
print(RED + "This is red text." + RESET)
print(GREEN + "This is green text." + RESET)
print(YELLOW + "This is yellow text." + RESET)
print(BLUE + "This is blue text." + RESET)
print(EXAMPLE + "This is a full example." + RESET)