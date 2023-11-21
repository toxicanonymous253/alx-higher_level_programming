#!/usr/bin/python3
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print("{} {}".format(self.brand, self.model))

car1 = Car('Toyota', 'Camry')
car2 = Car('Honda', 'Accord')

# Using the objects
car1.display_info()
car2.display_info()
