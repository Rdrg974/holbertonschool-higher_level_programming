#!/usr/bin/python3
"""Class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize Square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
