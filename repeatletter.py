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



