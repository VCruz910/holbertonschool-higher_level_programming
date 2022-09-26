#!/usr/bin/python3
"""
Module: Say My Name
A function that prints
the first name and last
name.
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print first and
    last names.

    Arguments:
        first_name: First Name.
        last_name: Last Name.
    Returns:
        No Return in this function.
    Raises:
        TypeError:
        - If first_name and/or last_name
        is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
