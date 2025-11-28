def count_vowel(s):
    return sum(1 for x in s.lower() if x in 'aeiou')
print(count_vowel('LKJHGFHGFDSAQeio'))

double = lambda x: x * 2
print(double(2))

str = '''I'm "Vishnumaya"'''
print(str)

string=input(":enter string::").lower()
vowel_count=0
con_count=0

vowels='aeiou'
for letter in string:
    if letter.isalpha():
        if letter in vowels:
            vowel_count+=1
        else:
            con_count+=1

print(vowel_count,con_count)
