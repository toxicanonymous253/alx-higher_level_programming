#!/usr/bin/python3
import random
import math

numlist = []

for i in range(5):
    numlist.append(random.randrange(1, 10))
for i in numlist:
    print(i, end=", ")
print()

i = len(numlist) - 1

while i > 0:
    j = 0
    while j < i:
        # ascending order
        if numlist[j] > numlist[j+1]:
            temp = numlist[j]
            numlist[j] = numlist[j + 1]
            numlist[j + 1] = temp
        j+=1
    i-=1

for k in numlist:
    print(k, end=", ")
print()
