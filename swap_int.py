a = int(input("Enter a: "))
b = int(input("Enter b: "))

temp = a
a = b
b = temp

print("After swapping: a =", a, "b =", b)


a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swapping: a =", a, "b =", b)
