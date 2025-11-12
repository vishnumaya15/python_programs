import random

words = ["apple", "banana", "cherry", "date"]
random.shuffle(words)
print(words)

# Alternate (without shuffle()):

import random

words = ["apple", "banana", "cherry", "date"]
shuffled = random.sample(words, len(words))
print(shuffled)




import random
str='abcdefghijkl'
print("STR",''.join(random.sample(str, len(str))))


import random
def shuffle_str(s):
    arr = list(s)
    random.shuffle(arr)
    return ''.join(arr)
print("shuffle_str",shuffle_str('mnopqrstuv'))




