#!/usr/bin/python3
"""
This module defines the MagicClass class
"""


import math


class MagicClass:
    """This class define a circle of a circumference."""
    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a given radius.

        Args:
            radius (float): The radius of the circle.
            Default value is 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
