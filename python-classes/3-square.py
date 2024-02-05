#!/usr/bin/python3
"""This module defines a class representing a square.

Raises:
    TypeError: size must be an intege
    ValueError: size must be >= 0

Returns:
    _type_: the current square area
"""


class Square:
    __size = None

    def __init__(self, __size):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    def area(self):
        return self.__size * self.__size
