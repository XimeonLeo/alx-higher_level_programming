#!/usr/bin/python3
""" Defines a function that prints a square

        Errors:
                TypeError: size must be an integer
                ValueErroe: size must be >= 0
                size must be an integer
"""


def print_square(size):
    """ The function that prints the Square
        Arguments:
                    size: The size of the square
        Return:
                Just prints the Square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size muat be an integer")
    for cm in range(size ** 2):
        if cm % size == 0 and cm != 0:
            print()
        print("#", end='')
    print()
