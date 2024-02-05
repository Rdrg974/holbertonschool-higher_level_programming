#!/usr/bin/python3
"""This module defines a class representing a square.

Raises
------
TypeError
    If the size provided is not an integer.
ValueError
    If the size provided is less than zero.
Returns
-------
int
    The area of the square.
tuple
    The position of the square's top-left corner.
Attributes
----------
size : int
    The size of the square's sides.
position : tuple of int
    The position of the square's top-left corner.
"""


class Square:
    """A class representing a square shape.

    Attributes
    ----------
    size : int
        The size of the square's sides.
    position : tuple of int
        The position of the square's top-left corner.
    """
    def __init__(self, __size=0, __position=(0, 0)):
        """Initialize the square."""
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
        if not isinstance(__position, tuple) or len(__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(type(i) is int and i >= 0 for i in __position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = __position

    @property
    def size(self):
        """int: The size of the square's sides."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square's sides."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """The position of the square's top-left corner."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square's top-left corner."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(type(i) is not int for i in value) or all(v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the size of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the given size and position."""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
