#!/usr/bin/python3
"""Creating an empty class to define a square."""


class Square:
    """
    Class that represents a square.

    Private Instance Attribute: size.
    Instantiation with optional size.
    Public Instance Method: def area(self).
    """

    def __init__(self, size=0):
        """Initialiazes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square's area."""
        return self.__size ** 2
