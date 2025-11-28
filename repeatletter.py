def repeat_string(s):
    count={}
    for letter in s:
        if letter in count:
            count[letter]+=1
        else:
            count[letter] =1
    print(count)
    max_char = max(count,key=count.get)
    print(max_char,"Count:", count[max_char])

    min_char = min(count,key=count.get)
    print(min_char,"Count:", count[min_char])
    for ch, freq in count.items():
        if freq > 2:
            print(ch, freq)
    
print(repeat_string("pppouoeiwuyrrrrrrr"))


def repeat_string(s):
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1

    max_char = max(count, key=count.get)
    min_char = min(count, key=count.get)
    more_than_two = {ch: freq for ch, freq in count.items() if freq > 2}

    return {
        "counts": count,
        "max_char": (max_char, count[max_char]),
        "min_char": (min_char, count[min_char]),
        "more_than_two": more_than_two
    }

print(repeat_string("pppouoeiwuyrrrrrrr"))


word = input("enter the word")
count_l = {}

for char in word:
    if char in count_l:
        count_l[char] += 1
        
    else:
        count_l[char] = 1
        
print(count_l)


print('-----------------------------------')




my_dict = {'a': 1, 'b': 2, 'c': 3}

# Method 1: Using 'in'
if 'b' in my_dict:
    print("Key exists")

# Method 2: Using 'get'
if my_dict.get('b') is not None:
    print("Key exists")

# Method 1: Direct access (raises KeyError if not found)
value = my_dict['a']

# Method 2: Safe access (returns None or default if not found)
value = my_dict.get('a')           # returns 1
value = my_dict.get('z', 'NotFound')  # returns 'NotFound'

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        print("Dog barks")

class Cat(Animal):
    def speak(self):  # Overriding the speak method
        # Calling the superclass method before adding specific behavior
        super().speak()
        print("Cat meows")

# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

# Call the speak method on different objects
animal.speak()
dog.speak()
cat.speak()


from collections import Counter
counts = Counter(word)
print(counts)



