#!/usr/bin/python3
""" A module that creates an empty class """


class BaseGeometry:
    """ Defines a class BaseGeaometry """

    def area(self):
        """ Returns the area of what is to come """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the content of value """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
