#!/usr/bin/python3
""" Defines a module that returns the list 
    of available attributes and methods of an object:
"""


def lookup(obj):
    """ Return thes available attributes and mthd of an obj """
    return dir(obj)
