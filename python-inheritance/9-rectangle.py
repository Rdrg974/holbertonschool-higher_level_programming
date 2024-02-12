#!/usr/bin/python3
"""Class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of retangle"""
        return self.__width * self.__height

    def __str__(self):
        """Print"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
