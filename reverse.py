test =" I am a developer"
print(" ".join(test.split()[::-1]))

print(" ".join(reversed(test.split())))


print(test[::-1])

reverse = ""
for char in test:
    reverse = char + reverse
print ("Reverse",reverse)

test1="Vishnu"
print(test1[0]+test1[1:-1][::-1]+test1[-1])

print(" ".join(test.split()[::-1]))


print(" ".join(test.split()[::-1]))
print(" ".join(reversed(test.split())))