nums = [5, 2, 9, 1, 7]

# Using sorted() (returns a new list)

sorted_list = sorted(nums)
print(sorted_list)     # [1, 2, 5, 7, 9]

# Using sorted() in descending order

sorted_list = sorted(nums, reverse=True)
print(sorted_list)     # [9, 7, 5, 2, 1]

# Using list.sort() (modifies the original list)

nums.sort()
print(nums)            # [1, 2, 5, 7, 9]

# Using list.sort(reverse=True)

nums.sort(reverse=True)
print(nums)            # [9, 7, 5, 2, 1]

# Sort with a custom key (e.g., by last digit)

nums = [45, 22, 93, 14, 67]
sorted_list = sorted(nums, key=lambda x: x % 10)
print(sorted_list)     # [22, 93, 14, 45, 67]

# Using list.sort()
nums = [5, 2, 9, 1, 7]
nums.sort()            # sorts in-place
print(nums)            # [1, 2, 5, 7, 9]

# Descending:

nums.sort(reverse=True)
print(nums)            # [9, 7, 5, 2, 1]

