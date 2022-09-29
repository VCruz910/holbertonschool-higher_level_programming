#!/usr/bin/python3
"""
Module: 3-is_kind_of_class

function that returns 'True' if
the object is an instance of,
or if the object is an instance
of a class that inherited from,
the specified class; otherwise
'False'.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks the Object.

    Arguments:
        - obj: Argument for object.
        - a_class: Argument for
        Class Type.
    Returns:
        - True or False.
    Raises:
        - None.
    """
    return isinstance(obj, a_class)
