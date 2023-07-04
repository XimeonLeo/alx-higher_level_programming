#!/usr/bin/python3
""" Defining a class Rectqngle """


class Rectangle:
    """Building a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing attributes for the Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """ Using print() to print the Rectangle using (self.print_symbol) """
        for cm in range(self.area()):
            if cm % self.__width == 0:
                if cm != 0:
                    print()
            print(self.print_symbol, end='')
        return ""

    @classmethod
    def square(cls, size=0):
        """returns a new instance of Rectangle as a Square """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Comperes and returm the bigger of the two Rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    def __repr__(self):
        """ Returns a representation of the Rectangle as string"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Delete an instance of the Rectamgle """
        type(self).number_of_instances -= 1
        print(f"Bye rectangle...")
