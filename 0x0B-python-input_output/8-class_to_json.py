#!/usr/bin/python3
"""A module that returnts the dict if an obj for jasin serelization """


def class_to_json(obj):
    """ My function that returns __dict__

    Arg:
        obj: an instance of the class

    Return:
            a dictiinary of all public attributes of the class
    """
    return obj.__dict__
