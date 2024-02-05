#!/usr/bin/python3
"""This module defines a class representing a square.
"""


class Square:
    """A class to represent a square shape.

    Attributes:
        size (int): The size of the square's sides.
    """
    __size = None

    def __init__(self, __size):
        """Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square's sides.

        Raises:
            TypeError: If the size provided is not an integer.
            ValueError: If the size provided is less than zero.
        """
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    def area(self):
        """Calculates the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
