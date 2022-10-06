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

    Private Attributes/Methods:
    --------------------------------------
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation.

        Arguments:
            - list_dictionaries: List of dictionaries.
        Returns:
            - JSON representation of list.
        Raises:
            - TypeError:
                * If list_dictionaries is not a list
                of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        if (type(list_dictionaries) != list or
                not all(type(X) == dict for X in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of
        'list_objs' to a file.

        Arguments:
            - list_objs: List of instances who
            inherits of 'Base'.
        Returns:
            - None.
        Raises:
            - TypeError:
                * If list_objs is not a list
                of instances.
        """
        if list_objs is None or list_objs == []:
            JStr = "[]"
        else:
            JStr = cls.to_json_string([O.to_dictionary() for O in list_objs])
        FileName = cls.__name__ + ".json"
        with open(FileName, 'w') as F:
            F.write(JStr)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation.

        Arguments:
            - json_string: String representing a list
            of dictionaries.
        Returns:
            - List represented by 'json_string'.
        Raises:
            - TypeError:
                * If json_string is not a string.
        """
        Lst = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            Lst = json.loads(json_string)
        return (Lst)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates instances.

        Arguments:
            - dictionary: Double pointer to
            a dictionary.
        Returns:
            - Created Instance.
        Raises:
            - None.
        """
        if cls.__name__ == 'Rectangle':
            DumIns = cls(1, 1)
        elif cls.__name__ == 'Square':
            DumIns = cls(1)
        DumIns.update(**dictionary)
        return (DumIns)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        Arguments:
            - None.
        Returns:
            - List of Instances.
        Raises:
            - None.
        """

        FileName = cls.__name__ + ".json"
        Lst = []
        LstDICT = []

        if os.path.exists(FileName):
            with open(FileName, 'r') as F:
                S = F.read()
                LstDICT = cls.from_json_string(S)
                for D in LstDICT:
                    Lst.append(cls.create(**D))
        return (Lst)
