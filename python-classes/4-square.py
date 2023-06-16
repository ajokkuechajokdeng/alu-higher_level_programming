#!/usr/bin/python3
"""Module documentation.

Square class definition.
"""


class Square:
    """Class documentation.

    Represent a square.
    """

    def __init__(self, size=0):
        """Method documentation.

        Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Method documentation.

        Getter method to retrieve the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method documentation.

        Setter method to set the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method documentation.

        Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
