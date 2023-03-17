#!/usr/bin/python3
"""
This module defines a Square class that defines a square by:
- a private instance attribute size
- a private instance attribute position
- an __init__ method to instantiate objects
- a property to get the size attribute
- a property setter to set the size attribute
- a property to get the position attribute
- a property setter to set the position attribute
- a method that returns the area of the square
- a method that prints the square with the character #
"""

class Square:
    """
    A class that defines a square by:
    - a private instance attribute size
    - a private instance attribute position
    - an __init__ method to instantiate objects
    - a property to get the size attribute
    - a property setter to set the size attribute
    - a property to get the position attribute
    - a property setter to set the position attribute
    - a method that returns the area of the square
    - a method that prints the square with the character #
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size of the square

