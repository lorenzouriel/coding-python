# Using a for loop
words = ['hello', 'world', 'python']

upper_words = []
for word in words:
    upper_words.append(word.upper())


# Using list comprehension
upper_words_lc = [word.upper() for word in words]

print(upper_words)    # Output: ['HELLO', 'WORLD', 'PYTHON']
print(upper_words_lc) # Output: ['HELLO', 'WORLD', 'PYTHON']
