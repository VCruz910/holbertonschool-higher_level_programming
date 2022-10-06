#!/usr/bin/python3
"""
Rectangle Class that
inherits from 'Base'
"""

# Imports for this Class:
import json
from models.base import Base


class Rectangle(Base):
    """
    Class that describes a rectangle.

    Attributes:
    =================================

    Public:
    _________________________________
    Public Instance Attribute:
        - width:
            * Property:
                # def width(self)
            * Property Setter:
                # def width(self, value)
        - height:
            * Property:
                # def height(self)
            * Property Setter:
                # def height(self, value)
        - x:
            * Property:
                # def x(self)
            * Property Setter:
                # def x(self, value)
        - y:
            * Property:
                # def y(self)
            * Property Setter:
                # def y(self, value)

    Public Instance Method:
        - area()
        - display()
        - to_dictionary()
        - update()

    Inherits from 'Base' Class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the instance.

        Arguments:
            - __width: width.
            - __height: height.
            - __x: X position.
            - __y: Y position.
            - id: id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Retrieves width attribute.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets width attribute to a value.

        Raises:
            - TypeError:
                * If width is not a integer.
            - ValueError:
                * If width's value is equal
                or less than zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves height attribute.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Sets height attribute to a value.

        Raises:
            - TypeError:
                * If height is not an integer.
            - ValueError:
                * If heigth's value is equal or
                less than zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves X position attribute.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Sets X attribute to a value.

        Raises:
            - TypeError:
                * If x is not an integer.
            - ValueError:
                * If x's value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves Y attribute.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Sets Y attribute to a value.

        Raises:
            - TypeError:
                * If Y is not an integer.
            - ValueError:
                * If Y's value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

# Mandatory Methods for Project:
    def area(self):
        """
        Returns Area Value of the Rectangle
        Instance.

        Returns:
            - Area of the instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in 'STDOUT' the Rectangle instance
        with the '#' chraracter.
        """
        for Ypos in range(0, self.__y):
            print()
        for INT_H in range(0, self.__height):
            for Xpos in range(0, self.__x):
                print(" ", end="")
            for INT_W in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representation of a
        Rectangle Instance.

        Returns:
            - Rectangle instance in
            string representation.
        """
        STR = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return (STR)

    def update(self, *args, **kwargs):
        """
        Assigns key/value arguments to
        attributes.

        Arguments:
            - args: Argument Pointer.
                * id: id attribute.
                * width: width attribute.
                * height: height attribute.
                * x: X position attribute.
                * y: Y position attribute.
        Raises:
            - TypeError:
                * If id is not an integer.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("ID must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for KEY, value in kwargs.items():
                if KEY == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("ID must be an integer")
                    self.id = value
                if KEY == "width":
                    self.width = value
                if KEY == "height":
                    self.height = value
                if KEY == "x":
                    self.x = value
                if KEY == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation
        of a Rectangle.
        """
        MyDICT = {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
        return (MyDICT)
