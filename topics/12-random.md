# Random
The random module **provides a suite of functions for generating pseudo-random numbers.** 

Here are some commonly used functions from the random module:

**1. Generating Random Numbers:**
- `random()`: Returns a random float in the range `(0.0, 1.0)`.
```python
import random

rand_num = random.random()
print(rand_num)
```

- `seed(x)`: Initialize the random number generator. If `x` is omitted or `None`, the current system time is used.
```python
import random

random.seed(42)  # Set a specific seed for reproducibility
rand_num = random.random()
print(rand_num)
```

- `shuffle(seq)`: Shuffles the elements of a sequence in place.
```python
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
```

- `choice(seq)`: Returns a randomly selected element from the given sequence.
```python
import random

my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(random_element)
```

- `sample(population, k)`: Returns a k-length list of unique elements chosen from the population sequence.
```python
import random

my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3)
print(random_sample)
```

- `The randrange()` function in the random module is used to generate a randomly chosen element from a range of values. It allows you to specify the start, stop, and step values for the range, and it returns a randomly selected element: `random.randrange([start, ] stop [, step])`
```python
import random

result = random.randrange(0, 10, 2)  # Random number from the range [0, 2, 4, 6, 8]
print(result)
```