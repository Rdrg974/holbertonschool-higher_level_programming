#!/usr/bin/python3
"""This is a module for a rectangle class."""


class Rectangle:
    """This is a class for a rectangle object."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This method constructs the object."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """This method returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """This method returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """This method returns the string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                          for _ in range(self.height)])

    def __repr__(self):
        """This method returns the string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """This method deletes the object."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
