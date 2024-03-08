list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
list3 = ['x', 'y']

result = zip(list1, list2, list3)

result_unzipped = zip(list1, list2, list3)
unzipped = list(zip(*result_unzipped))


print(list(result))  # Output: [(1, 'a', 'x'), (2, 'b', 'y')]
print(unzipped)