# rows= int(input("Rows"))
# columns=int(input("Columns"))

# for i in range (rows):
#     print(list("1"*columns))


# matrix = [list('1' * columns) for _ in range(rows)]
# print(matrix)


class Car:
    # Class attribute (shared by all Car objects)
    wheels = 4

    def __init__(self, make, model, color):
        # Instance attributes (unique to each Car object)
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print(f"The {self.color} {self.make} {self.model} is starting.")

    def stop(self):
        print(f"The {self.color} {self.make} {self.model} is stopping.")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "blue")
car2 = Car("Honda", "Civic", "red")

# Accessing attributes and calling methods on objects
print(f"Car 1: {car1.make} {car1.model}, Color: {car1.color}, Wheels: {car1.wheels}")
car1.start()

print(f"Car 2: {car2.make} {car2.model}, Color: {car2.color}, Wheels: {car2.wheels}")
car2.stop()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(f"Vector sum: ({v3.x}, {v3.y})")

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())