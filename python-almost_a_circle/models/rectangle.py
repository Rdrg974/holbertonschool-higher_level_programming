#!/usr/bin/python3
"""A class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A class Rectangle that inherits from Base"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): an integer. Defaults to 0.
            y (int): an integer. Defaults to 0.
            id (int): an integer. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
