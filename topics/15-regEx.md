# Regular Expressions (Regex)
**Regular expressions (regex or regexp) are powerful tools for pattern matching and text manipulation.** 

In Python, the `re` module provides support for regular expressions.

### Basic Patterns:
**1. Literal Characters:** Match the exact characters.
```python
import re

pattern = re.compile(r"hello")
match = pattern.match("hello world")
print(match.group())  # Output: hello
```

**2. Character Classes:** Match any one of a set of characters.
```python
pattern = re.compile(r"[aeiou]")
match = pattern.search("hello world")
print(match.group())  # Output: e
```

**3. Quantifiers:** Specify the number of occurrences.
```python
pattern = re.compile(r"\d{3}")
match = pattern.search("123456")
print(match.group())  # Output: 123
```


### Special Characters:
**1. `.` (Dot):** Matches any character except a newline.
```python
pattern = re.compile(r"he..o")
match = pattern.match("hello")
print(match.group())  # Output: hello
```

**2. `\d`, `\w`, `\s`:** Shorthand character classes (digit, word character, whitespace).
```python
pattern = re.compile(r"\d{2}-\w{3}-\d{4}")
match = pattern.match("29-Sep-2023")
print(match.group())  # Output: 29-Sep-2023
```


### Anchors:
**1. `^` (Caret):** Matches the start of a string.
```python
pattern = re.compile(r"^hello")
match = pattern.search("hello world")
print(match.group())  # Output: hello
```
	
**2. `$` (Dollar):** Matches the end of a string.
```python
pattern = re.compile(r"world$")
match = pattern.search("hello world")
print(match.group())  # Output: world
```


### Groups and Capturing:
**1. `( ... )`:** Create a group.
```python
pattern = re.compile(r"(\d{2})-(\w{3})-(\d{4})")
match = pattern.match("29-Sep-2023")
print(match.group(1))  # Output: 29
print(match.group(2))  # Output: Sep
print(match.group(3))  # Output: 2023
```


### Flags:
**1 `re.IGNORECASE` or `re.I`:** Case-insensitive matching.
```python
pattern = re.compile(r"hello", re.IGNORECASE)
match = pattern.match("HELLO")
print(match.group())  # Output: HELLO
```

### Functions:
- `re.search(pattern, string)`: Search for a pattern anywhere in the string.
- `re.match(pattern, string)`: Match the pattern only at the beginning of the string.
- `re.findall(pattern, string)`: Find all occurrences of the pattern in the string.
- `re.finditer(pattern, string)`: Find all occurrences of the pattern as an iterator of match objects.
- `re.sub(pattern, replacement, string)`: Replace occurrences of the pattern with the replacement string.

These are just some basic concepts, and regular expressions can get quite complex.

In the `src/regex.py` was created a code to validate a CPF, with default `input` and declared variable.