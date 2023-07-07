#!/usr/bin/python3
""" Defines a Function that prints the first and last name

        Errors:
                TypeError: if either of the names
                passed isnt a string
"""


def say_my_name(first_name, last_name=""):
    """ The function to Print f and l name
        Arguments:
            first_name: a string containing a name
            last_name: a string initialized to an empty
                    string if nothing is passer

        Return:
                It prints to standard output
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
