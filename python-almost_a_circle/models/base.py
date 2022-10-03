#!/usr/bin/python3
"""
Defines a Base Class for the other classes
in project.
"""

# imports for classes
import json
import csv
import os


class Base:
    """
    Base Class for the other classes.

    Attributes:
    ======================================
    Private Class Attribute: __nb_objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base Class Initialization.

        Arguments:
            - id: Instance ID.
        Returns:
            - None.
        Raises:
            - TypeError:
                * If id is not an integer.
        """
        if type(id) != int and id is not None:
            raise TypeError("ID must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
