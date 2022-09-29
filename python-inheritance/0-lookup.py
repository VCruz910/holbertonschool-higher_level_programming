#!/usr/bin/python3
"""
Module: Lookup.

Function that returns
the list of available
attributes and methods
of an object.
"""


def lookup(obj):
    """
    Function to return a list
    of available attributes.

    Arguments:
        - obj: Object that
        our code will look
        into.
    Returns:
        - A list object.
    Raises:
        - None.
    """
    return dir(obj)
