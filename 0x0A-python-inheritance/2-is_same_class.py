#!/usr/bin/python3
""" A module that checks if an object is
    exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ Returns True if the object and class are of the same instance
        Returns False if not

        Arguments:
                    obj: the object passed
                    a_class: the class to chexk
    """
    if type(obj) == a_class:
        return True
    return False
