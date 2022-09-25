#!/usr/bin/python3
"""Created an empty class that defines our square."""


class Square:
    """
    Class that represents a square.

    Private Instance Attribute: size.
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """
        Initializes the data for storing the square's size.

        Args:
            param1 (int): Size of the square.
        """
        self.__size = size
