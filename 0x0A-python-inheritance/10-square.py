#!/usr/bin/python3
""" A module that defines a subclass square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a subclass Square that inherits from Rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """ Returns the area of the square """

        return self.__size ** 2
