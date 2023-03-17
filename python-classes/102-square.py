#!/usr/bin/python3
"""
Module 4-square

Define a Square class
"""


class Square:
    """
    The class Square
    """
    def __init__(self, size=0):
        """
        Initialization of instances of Square class

        Args:
            size (int): Size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter of the private instance attribute size

        Return:
            The size of the Square instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of the private instance attribute size

        Args:
            value (int): Size of the square

        Raise:
            TypeError: If size is not a number (float or integer)
            ValueError: If size is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the Square instance

        Return:
            The area of the Square instance
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare if two Square instances are equal

        Args:
            other (Square): Another Square instance

        Return:
            True if both Square instances are equal, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare if two Square instances are not equal

        Args:
            other (Square): Another Square instance

        Return:
            True if both Square instances are not equal, False otherwise
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare if a Square instance is less than another
        Square instance

        Args:
            other (Square): Another Square instance

        Return:
            True if the Square instance is less than the 
            other Square instance, False otherwise
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare if a Square instance is less than or equal 
        to another Square instance

        Args:
            other (Square): Another Square instance

        Return:
            True if the Square instance is less than or equal
            to the other Square instance, False otherwise
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare if a Square instance is greater than another
        Square instance

        Args:
            other (Square): Another Square instance

        Return:
            True if the Square instance is greater than the 
            other Square instance, False otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare if a Square instance is greater than or equal
        to another Square instance

        Args:
            other (Square): Another Square instance

        Return:
            True if the Square instance is greater than or equal 
            to the other Square instance, False otherwise
        """
        return self.area() >= other.area()
