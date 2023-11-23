#!/usr/bin/python3
"""Defination of a class Square"""


class Square:
    """Represents a new square
    Args:
        size(int): The size of the new square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of the square"""
        return self.__size ** 2
