#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initializing a new Square """
        self.size = size

    @property
    def size(self):
        """Returns the current size of tne Square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the size of new Square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the Square """
        return (self.__size ** 2)
