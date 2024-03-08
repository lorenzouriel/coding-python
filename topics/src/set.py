# Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)  # or use the pipe operator: union_set = set1 | set2
print(union_set)

intersection_set = set1.intersection(set2)  # or use the ampersand operator: intersection_set = set1 & set2
print(intersection_set)

difference_set = set1.difference(set2)  # or use the minus operator: difference_set = set1 - set2
print(difference_set)


# Checking membership
result = 3 in set1
print(result)  # Output: False



# Iterating through a set
print("Time to iterate, my friend!")

for element in set2:
    print(element)