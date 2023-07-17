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
    def width(self, value):
        """ Sets the value for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the value for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Return the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the value for x """
        if type(value) != int:
            raise TypeError("x must be an intrger")
        elif value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ Returns the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the value for y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__height * self.__width

    def display(self):
        """ Prints the rectangle to stdout """
        for cm in range(self.area()):
            if cm % self.__width == 0:
                if cm != 0:
                    print()
            print('#', end='')
        print()

    def __str__(self):
        """ Returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        idd = self.id
        xx = self.__x
        yy = self.__y
        wit = self.__width
        hit = self.__height
        return f"[Rectangle] ({idd}) {xx}/{yy} - {wit}/{hit}"
