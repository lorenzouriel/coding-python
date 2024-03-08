import random

rand_num = random.random()
print(rand_num)


random.seed(42)  # Set a specific seed for reproducibility
rand_num = random.random()
print(rand_num)


my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)


my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(random_element)


my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3)
print(random_sample)


result = random.randrange(0, 10, 2)  # Random number from the range [0, 2, 4, 6, 8]
print(result)