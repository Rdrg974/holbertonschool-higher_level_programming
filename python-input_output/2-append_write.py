#!/usr/bin/python3
"""Append a string"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file"""
    with open(filename, "a") as f:
        return f.write(text)
