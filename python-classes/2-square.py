#!/usr/bin/python3
"""
This module contains one class:
    Square
"""


class Square:
    """
    This class defines a square
    """
    def __init__(self, size=0):
        """
        Initializes an object for the Square class.

        Args:
            size (int): size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
