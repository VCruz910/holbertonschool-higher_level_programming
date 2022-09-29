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

    Arguments:
        - list: Class List
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
        New_List = self[:]
        New_List.sort()
        print("{}".format(New_List))
