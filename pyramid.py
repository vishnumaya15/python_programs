rows = int(input("Enter rows"))

for i in range(1,rows+1):
    print(" " * (rows-i)+ "*"*(2*i-1))


for i in range(rows,0,-1):
    print(" " * (rows-i)+ "*"*(2*i-1))


for i in range(1, rows + 1):           # Outer loop → rows
    for j in range(1, 2 * rows):       # Inner loop → columns
        if j == rows - i + 1 or j == rows + i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()
