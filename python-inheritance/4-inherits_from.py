#!/usr/bin/python3
"""Check if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited"""
    return issubclass(type(obj), a_class)
