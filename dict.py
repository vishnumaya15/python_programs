key=[56,67,90]
values=['a','b','c']

print(dict(zip(key,values)))

d = {}
for i, k in enumerate(key):
    d[k] = values[i]
print(d)



d = {k: values[i] for i, k in enumerate(key)}
print('D',d)

d = dict([(key[i], values[i]) for i in range(len(key))])
print(d)


d1 = {}
for i in range(len(key)):
    d1[key[i]] = values[i]
print(d1)


class Calculator:
    def add(self, a, b=0):  # b has a default value
        return (a + b)

calc = Calculator()
print(calc.add(5))       # Output: 5 (b defaults to 0)
print(calc.add(5, 3))    # Output: 8


def process_data(fixed_arg1, fixed_arg2, *args, **kwargs):
    print(f"Fixed Arg 1: {fixed_arg1}")
    print(f"Fixed Arg 2: {fixed_arg2}")
    print(f"Positional Args: {args}")
    print(f"Keyword Args: {kwargs}")

process_data("hello", "world", 1, 2, 3, color="red", size="large")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
print_info(product="Laptop", price=1200, brand="Dell", warranty="1 year")