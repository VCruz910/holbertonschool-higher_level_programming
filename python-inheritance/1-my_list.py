#!/usr/bin/python3
"""
Module: 1-my_list
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
    Arguments:
        - list: Class list.
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
        print("{}".format(NList))
