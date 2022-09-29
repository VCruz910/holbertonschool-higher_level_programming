#!/usr/bin/python3
"""
Module: 2-is_same_class
Function that returns
'True' if object is
exactly an instance of
the specified class,
'False' if otherwise.
"""


def is_same_class(obj, a_class):
    return type(obj) is a_class
