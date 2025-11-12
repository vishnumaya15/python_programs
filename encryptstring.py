def encrypt_string(s):
    result=""
    count=1
    for i in range (1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            result += s[i-1]+str(count)
            count=1
    result+=s[-1]+str(count)
    return result

def  encrypted(s):
    result=""
    count=1
    for i in range(1,len(s)+1):
        if i<len(s) and s[i]==s[i-1]:
            count+=1
        else:
            result+=s[i-1]+str(count)
            count=1
    return result
print(encrypted('ppooiiuyytt'))


# def encrypt_string(s):
#     result = ""
#     count = 1

#     for i in range(1, len(s) + 1):
#         if i < len(s) and s[i] == s[i - 1]:
#             count += 1
#         else:
#             result += s[i - 1] + (str(count))
#             count = 1

#     return result

# # Example
# print(encrypt_string("saaavvvvvqqlll"))

