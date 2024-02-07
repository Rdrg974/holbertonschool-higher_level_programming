#!/usr/bin/python3
"""This is a module for a rectangle class."""


class Rectangle:
    """This is a class for a rectangle object."""
    def __init__(self, width=0, height=0):
        """This method constructs the object."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This property returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """This property sets the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This property returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """This property sets the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
