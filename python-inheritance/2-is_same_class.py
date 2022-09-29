#!/usr/bin/python3
"""
Module: 2-is_same_class.

Function that returns
'True' if object is
exactly an instance of
the specified class,
'False' if otherwise.
"""


def is_same_class(obj, a_class):
    """
    Checks if 'obj' is same as
    class or not.

    Arguments:
        - obj: Object Argument.
        - a_class: Class Type
        Argument.
    Returns:
        - True or False.
    Raises:
        - None.
    """
    return type(obj) is a_class
