#!/usr/bin/python3
"""
Module: 8-rectangle

Class that makes a
rectangle inherit
from BaseGeometry
class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle from
    BaseGeometry Class

    Instantiation with width and height:
        - def __init__(self, width, height):
    """

    def __init__(self, width, height):
        """
        Initializes instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
