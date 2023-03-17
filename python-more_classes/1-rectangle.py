#!/usr/bin/python3
"""
Module 1-rectangle

Contains class Rectangle with private attributes width and height
"""


class Rectangle:
    """
    Class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width of the rectangle

        Returns:
