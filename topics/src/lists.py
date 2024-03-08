# Creating a list
my_list = [1, 2, 3, "apple", "banana"]

# Accessing elements
print(my_list[0])      # Output: 1
print(my_list[3])      # Output: apple

# Modifying elements
my_list[0] = 100

# Adding elements
my_list.append("orange")
my_list.insert(0, "kiwi") # Position, Value

# Copy list
list1 = my_list[:]  # Copy the content of my_list into list1

# Remove elements
del list1[3]  # Remove element at index 3
list1.pop(3)  # Remove and return element at index 3

# Remove 'apple' from my_list
my_list.remove('apple')  # Remove the first occurrence of 'apple' from the list
list1.remove('banana')  # Remove the first occurrence of 'apple' from the list


# Print the updated lists
print("Updated list1:", list1)
print("Updated my_list:", my_list)