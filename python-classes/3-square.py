#!/usr/bin/python3
"""This module defines a class representing a square.

Raises:
    TypeError: If the size provided is not an integer.
    ValueError: If the size provided is less than zero.

Returns:
    int: The area of the square.

Attributes:
    size (int): The size of the square's sides.
"""


class Square:
    """A class to represent a square shape.

    Attributes:
        size (int): The size of the square's sides.
    """
    __size = None

    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    def area(self):
        return self.__size * self.__size
