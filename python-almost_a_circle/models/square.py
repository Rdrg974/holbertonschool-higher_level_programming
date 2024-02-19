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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute"""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
