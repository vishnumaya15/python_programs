num=int(input("Enter num"))
org=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if rev==org:
    print("palindrom")
else:
    print("not")





def ispalindrome(s):
    if s < 0 or (s%10 == 0 and s != 0):
        return False
    
    
    result = 0
    
    while s > result:
        digit = s % 10
        s = s // 10
        result = result * 10 + digit
        
        
    return s == result or s == result // 10
