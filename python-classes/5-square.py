#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """ Represents a square """

    def __init__(self, size=0):
        """ Initializes an instance of Square

        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ Gets the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of the square

        Args:
            value (int): size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with the character # """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
