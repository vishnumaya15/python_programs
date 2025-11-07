import random

words = ["apple", "banana", "cherry", "date"]
random.shuffle(words)
print(words)

# Alternate (without shuffle()):

import random

words = ["apple", "banana", "cherry", "date"]
shuffled = random.sample(words, len(words))
print(shuffled)