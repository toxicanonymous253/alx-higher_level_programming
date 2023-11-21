#!/usr/bin/python3
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print("My dog's name is {} and is {} years old".format(self.name, self.age))

my_dog = Dog("Chubby", 2)
my_dog.display_info()
