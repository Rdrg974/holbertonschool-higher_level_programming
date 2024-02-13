#!/usr/bin/python3
"""Write in the file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, "w") as f:
        return f.write(text)
