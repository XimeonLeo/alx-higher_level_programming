#!/usr/bin/python3
""" This module defines a class Base """


class Base:
    """ The Base of all other classes to be created """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize id Field """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
