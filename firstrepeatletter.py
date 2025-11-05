def first_repeat(s):
    frequency = None
    string_set = set()
    for letter in s:
        print(letter,"letter")
        if letter in string_set:
            frequency = letter
            print(frequency,"frequency")
            break
        string_set.add(letter)
    
    print(string_set,"string set")
    return frequency
print(first_repeat("tuippokk"))


def first_non_repeat(s):
    for letter in s:
        if s.count(letter)==1:
            return letter
    return None
print(first_non_repeat("pppwwweeoool"))