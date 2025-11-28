arr = [10,20,30,40,40,50]
maxnum = secondnum = float('-inf')
for num in arr:
    if num > maxnum:
        secondnum=maxnum
        maxnum=num
        
    elif num>secondnum and num!=maxnum:
        secondnum = num
print(secondnum)

arr.sort()
print(arr)
print(sorted(arr,reverse=True))
print(arr[-2])
print(sorted(arr)[-2])
print(sorted(set(arr))[-2])

arr.remove(max(arr))
print(max(arr))

