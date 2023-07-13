#!/usr/bin/python3
""" A module that checks if an obj is an instance of a class """


def inherits_from(obj, a_class):
    """ Returns True or False """

    return issubclass(type(obj), a_class) and type(obj) != a_class
