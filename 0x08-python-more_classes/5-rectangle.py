#!/usr/bin/python3
""" Defining a class Rectqngle """


class Rectangle:
    """Building a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing attributes for the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrive the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Update the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrive the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Update the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and return the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes and return the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Using print() to print the Rectangle using (#) """
        for cm in range(self.area()):
            if cm % self.__width == 0:
                if cm != 0:
                    print()
            print('#', end='')
        return ""

    def __repr__(self):
        """ Returns a representation of the Rectangle as string"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Delete an instance of the Rectamgle """
        print(f"Bye rectangle...")
