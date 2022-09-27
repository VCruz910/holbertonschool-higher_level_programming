
#!/usr/bin/python3
"""
Module: 1-rectangle.
Defines a rectangle
(based on 0-rectangle.py)
"""


class Rectangle:
    """
    Class to create and define a
    rectangle.
    Attributes:
    ===============================
    Private Instance Attribute: width:
        - Property: def width(self).
        - Property Setter: def width(self, value).
    Private Instance Attribute: height:
        - Property: def height(self).
        - Property Setter: def height(self, value).
    Istantiation with optional with and height:
        - def __init__(self, width=0, height=0):
    Public Instance Method: def area(self).
    Public Instance Method: def perimeter(self).
    Public Class Attribute: number_of_instances.
    Public Class Attribute: print_symbol:
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes our Rectangle's instance.
        Arguments:
            - width: Width of the rectangle.
            - height: Height of the rectangle.
        Returns:
            - None.
        Raises:
            - None.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns the Rectangle in '#'
        Character.
        Arguments:
            - None.
        Returns:
            - STR of the Rectangle.
        Raises:
            - None.
        """
        Rectangle = ""
        if self.height == 0 or self.width == 0:
            return ''
        RecSTR = ''
        for I in range(self.height):
            for J in range(self.width):
                RecSTR += str(self.print_symbol)
            RecSTR += '\n'
        return RecSTR[:-1]

    def __repr__(self):
        """
        Returns a string representation of the
        rectangle that is also able to recreate
        a new instance by using eval().
        Arguments:
            - None.
        Returns:
            - String representation of the
            Rectangle.
        Raises:
            - None.
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        Deletes the rectangle.
        Arguments:
            - None.
        Returns:
            - None.
        Instances:
            - None.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # Width Property and Setter.
    @property
    def width(self):
        """
        Returns the Width Value of our
        rectangle.
        Arguments:
            - None.
        Returns:
            - The Width of the rectangle.
        Raises:
            - None.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Defines the Width of the
        rectangle.
        Arguments:
            - value: width of the rectangle.
        Returns:
            - None.
        Raises:
            - TypeError:
                * If the Rectangle's width
                is not an integer.
            - ValueError:
                * If the Rectangle's value
                is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Height Property and Setter
    @property
    def height(self):
        """
        Returns the Height Value of
        the rectangle.
        Arguments:
            - None.
        Returns:
            - The height of the
            rectangle.
        Raises:
            - None.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Defines the Height of
        the rectangle.
        Arguments:
            - value: Height of the Rectangle.
        Returns:
            - None.
        Raises:
            - TypeError:
                * If the height of the Rectangle
                is not an integer.
            - ValueError:
                * It the height value of the
                Rectangle is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the Rectangle's
        area.
        Arguments:
            - None.
        Returns:
            - Area of the Rectangle.
        Raises:
            - None.
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Calculates the Rectangle's
        perimeter.
        Arguments:
            - None.
        Returns:
            - Perimeter of the Rectangle.
        Raises:
            - None.
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))
