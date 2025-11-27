str=input("ENter string::").lower()

char='h'
count=0
for letter in str:
    if letter==char:
        count+=1
print(count)