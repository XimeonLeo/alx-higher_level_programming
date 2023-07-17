#!/usr/bin/python3
""" This module creates a class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Defines a subclass Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the value for width """
        self.__width = width

    @property
    def height(self):
        """ Returns the value for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the value for height """
        self.__height = height

    @property
    def x(self):
        """ Return the value of x """
        return self.__x

    @x.setter
    def x(self, x):
        """ sets the value for x """
        self.__x = x

    @property
    def y(self):
        """ Returns the value of y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Sets the value for y """
        self.__y = y
