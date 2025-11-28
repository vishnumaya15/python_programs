def encrypt_String(s):
    result=""
    count=1
    for i in range (1,len(s)+1) :
        if i<len(s) and s[i] == s[i-1]:
            count+=1
        else:
            result+=s[i-1] + (str(count) if count>1 else "")  #str(count) becuase we can't add str+int
            count=1
    return result
print(encrypt_String('pppoooiiuuyyttrr'))

s='ppooiiuuyy'
# i is index
for i in range(1, len(s)):
    print(s[i], s[i-1])  # can compare current and previous

# i is character
for i in s:
    print(i)  # only the character, no access to previous directly

