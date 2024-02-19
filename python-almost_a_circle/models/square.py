#!/usr/bin/python3
"""A class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialise.

        Args:
            size (int): the size of square
            x (int): an integer. Defaults to 0.
            y (int): an integer. Defaults to 0.
            id (int): an integer. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
