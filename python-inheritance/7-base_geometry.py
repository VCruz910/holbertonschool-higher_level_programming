#!/usr/bin/python3
"""
Module: 7-base_geometry

Class that defines the
attributes of Shapes.
"""


class BaseGeometry:
    """
    Defines the attributes of
    Geometric Shapes.

    Attributes:
    =========================
    Public Instance Method: def area(self).
    Public Instance Method: def integer_validator(self, name, value).
    """

    def area(self):
        """
        Defines the area of a geomtric shape.

        Arguments:
            - None.
        Returns:
            - None.
        Raises:
            - Exception:
                * raises an Exception with the
                message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Recieves the value property of
        the geometric shape.

        Arguments:
            - name: Name of the object.
            - value: Value of the property.
        Returns:
            - None.
        Raises:
            - TypeError:
                * If value is not an integer.
            - ValueError:
                * If value is less or equal
                than zero.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
