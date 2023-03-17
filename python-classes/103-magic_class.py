#!/usr/bin/python3
"""
This module defines the MagicClass class
"""


import math


class MagicClass:
    """
    This class defines a circle with a given radius and provides methods to calculate its area and circumference.
    """
    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a given radius.

        Args:
            radius (float): The radius of the circle. Default value is 0.

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

