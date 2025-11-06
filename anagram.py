# Method 1: Using sorted()
def is_anagram1(s1, s2):
    return sorted(s1) == sorted(s2)


# Method 2: Using Counter
from collections import Counter
def is_anagram2(s1, s2):
    return Counter(s1) == Counter(s2)


# Method 3: Manual count using dictionary
def is_anagram3(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True


# Method 4: Using set and count
def is_anagram4(s1, s2):
    return set(s1) == set(s2) and all(s1.count(c) == s2.count(c) for c in set(s1))


# Method 5: Using ASCII sum (only works if unique char counts match)
def is_anagram5(s1, s2):
    return sum(map(ord, s1)) == sum(map(ord, s2))


# Example
print(is_anagram1("listen", "silent"))
print(is_anagram2("listen", "silent"))
print(is_anagram3("listen", "silent"))
print(is_anagram4("listen", "silent"))
print(is_anagram5("listen", "silent"))
