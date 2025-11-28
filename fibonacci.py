def fibonacci(n):
    if n <= 1:
        return n
    # elif n == 1:
    #     return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

def fibonacci_iterative(n):
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(a)
    else:
        print(a, end=" ")
        print(b, end=" ")
        for _ in range(2, n):
            next_fib = a + b
            print(next_fib, end=" ")
            a = b
            b = next_fib

fibonacci_iterative(10)

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci_iterative(10)

def fibonacci_recursive(n):
    for i in range(num_terms):
        if n <= 1:
            return n
        else:
            return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

num_terms = 20
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    for i in range(num_terms):
        print(fibonacci_recursive(i), end=" ")

def fibb(n):
    a,b=0,1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b
fibb(10)

def fibbo(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibbo(10))

def fiba(n):
    if n<=1:
        return n
    else:
        return fiba(n-1)+fiba(n-2)
print("lll",fiba(10))
    
