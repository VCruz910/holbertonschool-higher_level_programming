#!/usr/bin/python3
"""
Module: 9-rectangle

Class that inherits from
BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle from BaseGeometry Class.
    """

    def __init__(self, width, height):
        """
        Initializes instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the instance.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the printable string.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
