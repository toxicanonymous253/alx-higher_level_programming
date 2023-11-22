#!/usr/bin/python3
from mutators import P
p1 = P(42)
p2 = P(4711)
print(p1.get_x())
p1.set_x(47)
p1.set_x(p1.get_x() + p2.get_x()) # Javaesque expression
print(p1.get_x())
