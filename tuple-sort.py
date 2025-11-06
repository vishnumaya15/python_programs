tup = (5, 2, 9, 1, 7)

#  Using sorted() (returns a list)

sorted_list = sorted(tup)
print(sorted_list)     # [1, 2, 5, 7, 9]

# Convert back to tuple

sorted_tuple = tuple(sorted(tup))
print(sorted_tuple)    # (1, 2, 5, 7, 9)

# Sort descending

sorted_tuple = tuple(sorted(tup, reverse=True))
print(sorted_tuple)    # (9, 7, 5, 2, 1)

# Custom key (example: sort by even numbers first)

sorted_tuple = tuple(sorted(tup, key=lambda x: x % 2))
print(sorted_tuple)    # (2, 5, 9, 1, 7)


# Tuples are immutable, so you must convert them to a list first:

tup = (5, 2, 9, 1, 7)
lst = list(tup)
lst.sort()
tup = tuple(lst)
print(tup)  # (1, 2, 5, 7, 9)