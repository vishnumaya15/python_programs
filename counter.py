from collections import Counter

# 1. Count frequency of elements
print("1.", Counter([1, 2, 2, 3, 3, 3]))

# 2. Count characters in a string
print("2.", Counter("banana"))

# 3. Find most common elements
c = Counter("banana")
print(c)
print("3.", c.most_common(1))
print("3.", c.most_common(2))

# 4. Add / Subtract Counters
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print("4. Add:", c1 + c2)
print("4. Subtract:", c1 - c2)

# 5. Intersection & Union
print("5. Intersection:", c1 & c2)
print("5. Union:", c1 | c2)

# 6. Count words in a sentence
words = "this is a test this is only a test".split()
print("6.", Counter(words))

# 7. Frequency analysis (example)
log_data = ["error", "info", "warning", "error", "error", "info"]
print("7.", Counter(log_data))

# 8. Convert Counter back to list
c3 = Counter(a=3, b=1)
print("8.", list(c3.elements()))

# 9. Compare frequencies (anagram check)
print("9.", Counter("listen") == Counter("silent"))

# 10. Remove zero or negative counts
c4 = Counter(a=2, b=-1)
c4 += Counter()
print("10.", c4)
