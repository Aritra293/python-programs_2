import itertools
number = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", number)
number.sort()
new_num = list(number for number,_ in itertools.groupby(number))
print("New List", new_num)
