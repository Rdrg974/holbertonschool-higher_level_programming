#!/usr/bin/python3
"""Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of square"""
        return self.__size**2

    def __str__(self):
        """Print"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
