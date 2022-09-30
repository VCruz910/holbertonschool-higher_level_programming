#!/usr/bin/python3
"""
Module: 11-square.

Square class that inherits
from the Rectangle Class
based on 10-square module.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a Square from Rectangle class.
    """
    def __init__(self, size):
        """
        Initializes a Square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Returns a string with the area.
        """
        return super().area()

    def __str__(self):
        """
        Returns a printable string.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
