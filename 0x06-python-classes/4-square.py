#!/usr/bin/python3
class Square:
    """A class to represent a square."""

    def __init__(self, size=0):
        """
        Initialize the Square object.

        Parameters:
        size (int, optional): The size of the square. Defaults to 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.

        """
        return self.__size ** 2
