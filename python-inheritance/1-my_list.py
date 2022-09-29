#!/usr/bin/python3
"""
Module: My List.
Class that inherits
from 'list'.
"""


class MyList(list):
    """
    Class for organizing
    lists.

    Attributes:
    ====================
    Public Instance Method:
        - def print_sorted(self):
    """
    def print_sorted(self):
        """
        Prints our list in
        ascending order.

        Arguments:
            - None.
        Returns:
            - None.
        Raises:
            - None.
        """
        NList = self[:]
        NList.sort()
        print(f"{NList}")
