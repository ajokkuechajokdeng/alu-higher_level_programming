#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    A class to represent a square.

    Attributes:
    -----------
    size : int
        The size of the square
    """

    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the Square object.

        Parameters:
        -----------
            size : int, optional
                The size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """
        Getter function to retrieve the size of the square.

        Returns:
        --------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter function to set the size of the square.

        Parameters:
        -----------
        value : int
            The size of the square.

        Raises:
        -------
        TypeError:
            If the size is not an integer.
        ValueError:
            If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        --------
        int
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to the standard output.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
