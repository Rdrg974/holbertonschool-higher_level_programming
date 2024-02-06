#!/usr/bin/python3
"""Function that adds 2 integers.

Returns:
        _type_: the sum of a and b
"""


def add_integer(a, b=98):
    """ Add 2 integers
    Sum of a and b
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a + b)
