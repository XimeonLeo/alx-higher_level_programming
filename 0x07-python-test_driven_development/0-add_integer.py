#!/usr/bin/python3
"""
    Definea a funtion that adds two integers

    Raise a TypeError is a or b is not an integer
"""


def add_integer(a, b=98):
    """
        Returns the sum of two intrgers and cast float into an int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
