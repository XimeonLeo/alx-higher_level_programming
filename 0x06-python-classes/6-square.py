#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new Square """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Returns the tuple for the Square """
        return self.__position

    @position.setter
    def position(self, value):
        """ Checking and setting for a valid tuple """
        try:
            if isinstance(value, tuple):
                x, y = value
                if isinstance(x, int) and isinstance(y, int):
                    if x >= 0 and y >= 0:
                        self.__position = value
        except Exception:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the area of the Square """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints out the square (modified) """
        if self.__size == 0:
            print()

        for y in range(self.__position[1]):
            print()
        for cm in range(self.__size ** 2):
            if cm % self.__size == 0:
                if cm != 0:
                    print()
                for x in range(self.__position[0]):
                    print(" ", end='')
            print("#", end='')
        print()
