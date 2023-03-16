class Square:
    def __init__(self, size=0):
        """Initialize a new instance of the Square class."""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
