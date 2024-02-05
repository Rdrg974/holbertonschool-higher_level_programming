#!/usr/bin/python3
"""This module defines a class representing a square.
"""


class Square:
    """This class represents a square.
    """
    __size = None

    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
