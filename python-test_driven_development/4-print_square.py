#!/usr/bin/python3
"""Print a square with the character #."""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): The size of the square to print

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
