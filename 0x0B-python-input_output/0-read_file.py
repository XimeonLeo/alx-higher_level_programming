#!/usr/bin/python3
""" Defines a module that reads from a file """


def read_file(filename=""):
    """
        Argument:
                filename: the name of the file to open
        Opens and read a file to stdout
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        print(my_file.read(), end='')
