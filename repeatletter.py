def repeat_string(s):
    count_string={}
    for letter in s:
        if letter in count_string:
            count_string[letter]+=1
        else:
            count_string[letter] =1
    print(count_string)
    max_char = max(count_string,key=count_string.get)
    print(max_char,"Count:", count_string[max_char])

    min_char = min(count_string,key=count_string.get)
    print(min_char,"Count:", count_string[min_char])

    
print(repeat_string("pppouoeiwuyrrrrrrr"))
