lst = [1, 2, 3, 2, 4, 1, 5]
unique_list = []

for item in lst:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

lst = [1, 2, 3, 2, 4, 1, 5]
lst.sort()
unique_list = [lst[0]]

for i in range(1, len(lst)):
    if lst[i] != lst[i-1]:
        unique_list.append(lst[i])

print(unique_list)