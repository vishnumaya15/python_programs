# Sample dictionary
data = {'b': 5, 'a': 2, 'd': 8, 'c': 1}

# Sort by keys (ascending)

sorted_dict = dict(sorted(data.items()))
print(sorted_dict)   # {'a': 2, 'b': 5, 'c': 1, 'd': 8}

# Sort by keys (descending)

sorted_dict = dict(sorted(data.items(), reverse=True))
print(sorted_dict)

# Sort by values (ascending)

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_dict)

# Sort by values (descending)

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)

# Using operator.itemgetter

from operator import itemgetter
sorted_dict = dict(sorted(data.items(), key=itemgetter(1)))  # sort by value
print(sorted_dict)

# Using dictionary comprehension

sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda x: x[1])}
print("dictionary comprehension",sorted_dict)

# Sort only keys or values separately

print(sorted(data.keys()))    # ['a', 'b', 'c', 'd']
print(sorted(data.values()))  # [1, 2, 5, 8]