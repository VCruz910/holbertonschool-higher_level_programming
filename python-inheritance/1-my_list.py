#!/usr/bin/python3
"""Class that inherits from list."""


class MyList(list):
    """Class for organizing lists."""
    def print_sorted(self):
        """Prints our list in ascending order."""
        print(sorted(self))
