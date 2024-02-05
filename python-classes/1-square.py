#!/usr/bin/python3
"""This module defines a class representing a square.
"""


class Square:
    """This class represents a square
    """
    __size = None

    def __init__(self, __size):
        if isinstance(__size, int):
            self.__size = __size
        else:
            return None
