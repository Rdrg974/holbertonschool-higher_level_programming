#!/usr/bin/python3
"""Read the file"""


def read_file(filename=""):
    """Fonction who read a file"""
    with open(filename, "r") as f:
        print(f.read(), end='')
