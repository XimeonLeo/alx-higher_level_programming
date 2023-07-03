#!/usr/bin/python3
""" Defining a class Rectqngle """


class Rectangle:
    """ Building a Rectangle  """
    def __init__(self, width=0, height=0):
        """ Initializing attributes for the Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrive the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Update the width of the Rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrive the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Update the height of the Rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
