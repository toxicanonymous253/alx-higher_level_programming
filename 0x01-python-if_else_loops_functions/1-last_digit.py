#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

remNumber = abs(number) % 10

if remNumber > 5:
	print(f"Last digit of {number} is {remNumber} and is greater than 5")
elif remNumber == 0:
	print(f"Last digit of {number} is {remNumber} and is 0")
elif remNumber < 6 and remNumber != 0:
	print(f"Last diigt if {number} is {remNumber} and is less than 6 and not 0")
else:
	pass
