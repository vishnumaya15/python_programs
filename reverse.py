test =" I am a developer"
print(" ".join(test.split()[::-1]))

print(" ".join(reversed(test.split())))


print(test[::-1])

reversed = ""
for char in test:
    reversed = char + reversed
print ("Reverse",reversed)

test1="Vishnu"
print(test1[0]+test1[1:-1][::-1]+test1[-1])

print(" ".join(test.split()[::-1]))