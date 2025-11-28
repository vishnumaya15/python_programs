def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


a = [1, 2, 3] 
b = [1, 3, 5] 
# print(a - b) 
print(a + b)  
print(a * b)