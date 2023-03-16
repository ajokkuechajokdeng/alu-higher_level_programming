#!/usr/bin/python3
"""
Module - 1-square
Defines a class Square with a private instance attribute size
"""


class Square:
    """
    A class Square with private instance attribute size
    """
    def __init__(self, size):
        """
        Initialize a new Square with the given size

        Args:
        size (int): The size of the new square object.

        Returns:
        None
        """
        self.__size = size
