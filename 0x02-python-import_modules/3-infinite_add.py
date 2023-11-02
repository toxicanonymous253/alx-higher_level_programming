#!/usr/bin/python3
import sys
sum = 0
if len(sys.argv) == 1:
    print("0")
if len(sys.argv) > 2:
    for i in range(1, len(sys.argv)):
        result = int(sys.argv[i])
        sum += result
print("{:d}".format(sum))
