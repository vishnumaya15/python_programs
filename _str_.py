class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"  #2023 Toyota Camry
    # def print_output(self):
    #     return f"{self.year} {self.make} {self.model}"  <__main__.Car object at 0x7f27088b5c10>

my_car = Car("Toyota", "Camry", 2023)
print(my_car)  # Output: 2023 Toyota Camry