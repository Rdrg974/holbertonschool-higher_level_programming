#!/usr/bin/python3
"""A class MyInt"""


class MyInt(int):
    """A class MyInt"""
    def __eq__(self, other):
        """equal equal method"""
        return super().__eq__(other)
    
    def __ne__(self, other):
        """not equal method"""
        return super().__ne__(other)
