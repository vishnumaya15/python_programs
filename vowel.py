def count_vowel(s):
    return sum(1 for x in s.lower() if x in 'aeiou')
print(count_vowel('LKJHGFHGFDSAQeio'))

double = lambda x: x * 2
print(double(2))