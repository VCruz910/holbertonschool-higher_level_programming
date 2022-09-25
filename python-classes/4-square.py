#!/usr/bin/python3
"""Created an empty class that defines the project's square."""


class Square:
    """
    Empty class that defines the square.

    Attributes:
    --------------------------------
    Private Instance Attribute: size.
        - Property def size(self)
        - Property Setter def size(self, value)
    Istantiation with optional size.
    Public Instance Method: def area(self).
    """

    def __init__(self, size=0):
        """Initializes our data for the square."""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of our square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of our square to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns our current square's area."""
        return self.__size ** 2
