# Terminal Colors
In Python, we can design our terminal with colors, providing an improved user experience and code understanding.

The sequence is: `\033m[Style;Text;Background m`
- Style - Font
- Text - Text Color
- Background

```python
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
```

### Below is the table with values and formatting code:
| Style            | Text        | Background      |
|------------------|-------------|-----------------|
| 0 - None         | 30 - White  | 40 - White      |
| 1 - Bold         | 31 - Red    | 41 - Red        |
| 4 - Underline    | 32 - Green  | 42 - Green      |
|                  | 33 - Yellow | 43 - Yellow     |
|                  | 34 - Blue   | 44 - Blue       |
|                  | 35 - Purple | 45 - Purple     |
|                  | 36 - Cyan   | 46 - Cyan       |
|                  | 37 - Gray   | 47 - Gray       |
