num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

index = 0
max_index = 0
max_sum = 0
for list in num:
    sum_list = 0
    for x in list:
        sum_list += x
    if sum_list > max_sum:
        max_sum = sum_list
        max_index = index
    index += 1

print(num[max_index])