#!/usr/bin/python3
"""Function that adds 2 integers."""


def add_integer(a, b=98):
    """Add 2 integers.

    Args:
        a (int, float): a integer
        b (int, float): an integer. Defaults to 98.

    Raises:
        TypeError: a and b must be an integer

    Returns:
        _type_: the sum of a and b
    """
    if not (isinstance(a, (int, float)) or isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, (int, float)) or isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
