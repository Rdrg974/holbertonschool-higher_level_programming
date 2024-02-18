#!/usr/bin/python3
"""A class Base."""


class Base:
    """A clase Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise.

        Args:
            id (int): an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
