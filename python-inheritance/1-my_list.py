#!/usr/bin/python3
"""Create a class MyList"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Print the list sorted"""
        print(sorted(self))
