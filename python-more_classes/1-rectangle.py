#!/usr/bin/python3
"""
Module 1-rectangle

Contains class Rectangle
with private instance attributes width and height
and public methods area and perimeter
"""


class Rectangle:
    """
    Class Rectangle
    Defines a rectangle with private instance attributes width and height
    and public methods area and perimeter
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
