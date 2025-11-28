rows = int(input("Enter rows"))

for i in range(1,rows+1):
    print(" " * (rows-i)+ "*"*(2*i-1))
print("1------------------------------------------------")
for i in range(rows,0,-1):
    print(" " * (rows-i)+ "*"*(2*i-1))
print("2------------------------------------------------")
for i in range(1, rows + 1):           # Outer loop → rows
    for j in range(1, 2 * rows):       # Inner loop → columns
        if j == rows - i + 1 or j == rows + i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("3------------------------------------------------")
for i in range (rows+1):
    for j in range (1,i+1):
        print("*",end ="")
    print()
print("4------------------------------------------------")
for i in range(rows, 0, -1):      # start from rows, go down to 1
    for j in range(1,i+1):
        print("*", end="")
    print()
print("5------------------------------------------------")
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")      # spaces for alignment
    for j in range(1, 2 * i):            # numbers increasing
        print(j, end="")
    print()
print("6------------------------------------------------")
for i in range(1,rows+1):
    for j in range (rows-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
print("7------------------------------------------------")
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
print("8------------------------------------------------")
for i in range (1,rows+1):
    for j in range(1,rows+1):
        if i==1 or i== rows or j==1 or j==rows:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("9------------------------------------------------")
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if j==1 or i==rows or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range (1,rows+1):
    for j in range(1,rows+1):
        if i==1 or i== rows or j==1 or j==rows:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(1,rows+1):
    for j in range(1,rows+1):
        if j==1 or i==rows or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()