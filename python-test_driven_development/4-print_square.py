#!/usr/bin/python3
"""
Module: Print Square.
Prints a square with
the '#' character.
"""


def print_square(size):
    """
    Function to print our square.

    Arguments:
        -Size: The size lenght of
            the printed square.
    Returns:
        No returns in this function.
    Raises:
        -TypeError:
            * If the size of the square
            is not an integer/float
            number.
        -ValueError:
            * If the size of the square
            is less than zero.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and len(size) < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for Num in range(size):
        print("#" * size)
