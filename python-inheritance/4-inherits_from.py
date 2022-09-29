#!/usr/bin/python3
"""
Module: 4-inherits_from

Function that returns 'True'
if the object is an instance
of a class that inherited
(directly or indirectly)
from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an
    instance inherited.

    Arguments:
        - obj: Object Argument.
        -a_class: Class Type
        Argument.
    Returns:
        - True or False.
    Raises:
        - None.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
