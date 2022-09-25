#!/usr/bin/python3
"""Created an empty class to define a square."""


class Square:
    """
    Class to define a square.
    Attributes:
    ------------------------
    Private Instance Attribute: size:
        - Property def size(self)
        - Property Setter def size(self, value)
    Private Instance Attribute: position:
        - Property def position(self)
        - Property Setter def position(self, value)
    Instantiation with optional size.
    Public Instance Method: def area(self).
    Public Instance Method: def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialez the data for the square."""
        self.__size = size
        self.__position = position

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
    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of a square to a value."""
        if not isinstance(value, tuple) or len (value) != 2:
            raise TypeError("position must be a tuple of 2 positive")
        if not isinstance(value[0], int) or not isinstance(value[1],int):
            raise TypeError("position must be a tuple of 2 positive")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive")
        else:
            self.__position = value

    def area(self):
        """Returs the area of the current square."""
        return self.__size **2

    def my_print(self):
        """
        Prints to STOUT the square with the '#' character,
        at the position given by the Position Attribute.
        """
        if self.__size == 0:
            print()
            return
        for Y in range(0, self.__position[1]):
            print()
        for I in range(0, self.__size):
            for X in range(0, self.position[0]):
                print(" ", end="")
            for J in range(0, self.__size):
                print("#", end="")
            print()
