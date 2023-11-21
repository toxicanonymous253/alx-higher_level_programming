#!/usr/bin/python3
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person('Dave')
p.say_hi()

#The previous 2 lines can be written as
#Person('Dave').say_hi()
