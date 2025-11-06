def countdown(n):

    while n > 0:

        yield n

        n -= 1

for number in countdown(5):

    print(number)


#Call by value
def modify_string(s):
    s = "world"  # A new string object is created, 's' now points to it
    print(f"Inside function: {s}")

my_string = "hello"
modify_string(my_string)
print(f"Outside function: {my_string}")


# Call by reference
def modify_list(l):
    l.append(4)  # Modifies the original list object
    print(f"Inside function: {l}")

my_list = [1, 2, 3]
modify_list(my_list)
print(f"Outside function: {my_list}")