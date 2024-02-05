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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __init__(self, __size=0):
        self.__size = __size

    def area(self):
        return self.__size * self.__size
