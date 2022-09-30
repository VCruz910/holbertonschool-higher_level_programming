#!/usr/bin/python3
"""
Module: 1-my_list
Class that inherits
from list.
"""


class MyList(list):
    """Class for organizing lists."""
    def print_sorted(self):
        """Prints our list in ascending order."""
        print(sorted(self))
