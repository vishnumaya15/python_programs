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



