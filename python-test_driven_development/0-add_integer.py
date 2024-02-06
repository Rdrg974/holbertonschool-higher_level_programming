#!/usr/bin/python3
"""Function that adds 2 integers."""


def add_integer(a, b=98):
    
    if not (isinstance(a, (int, float)) or isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, (int, float)) or isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a)+ int(b)
