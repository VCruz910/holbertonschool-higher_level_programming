#!/usr/bin/python3
"""Created an empty class to define a square."""


class Square:
    """
    Class to define a square.

    Attributes:
    ------------------------
    Private Instance Attribute: size.
        - Property def size(self)
        - Property Setter def size(self, value)
    Instantiation with optional size.
    Public Instance Method: def area(self).
    Public Instance Method: def my_print(self).
    """

    def __init__(self, size=0):
        """Initialez the data for the square."""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returs the area of the current square."""
        return self.__size **2

    def my_print(self):
        """Prints to STOUT the square with the '#' character."""
        if self.__size == 0:
            print()
        else:
            for INT_A in range(0, self.__size):
                for INT_B in range(0, self.__size):
                    print("#", end="")
                print()
