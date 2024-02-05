#!/usr/bin/python3
"""This module defines a class representing a square.

Raises:
    TypeError: If the size provided is not an integer.
    ValueError: If the size provided is less than zero.

Returns:
    int: The area of the square.

Attributes:
    size (int): The size of the square's sides.
    position (tuple of int): The position of the square's top-left corner
"""


class Square:
    """A class representing a square shape.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple of int): The position of the square's top-left corner.
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

    __position = None

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or not all(v >= 0 for v in value) or \
                len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __init__(self, __size=0, __position=(0, 0)):
        self.__size = __size
        self.__position = __position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
