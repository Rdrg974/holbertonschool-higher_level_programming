#!/usr/bin/python3
"""Create a class MyList"""


class MyList(list):
    
    def __init__(self):
        """Initializes the object"""
        pass

    def print_sorted(self):
        """Print the list sorted"""
        print(sorted(self))
