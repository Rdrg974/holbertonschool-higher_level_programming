#!/usr/bin/python3
"""A class MyInt"""


class MyInt(int):
    """A class MyInt"""
    def __eq__(self, other):
        """A class MyInt"""
        return int(self) != int(other)

    def __ne__(self, other):
        """A class MyInt"""
        return int(self) == int(other)
