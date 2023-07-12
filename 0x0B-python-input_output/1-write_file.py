#!/usr/bin/python3
""" A module that writes into a file """


def write_file(filename="", text=""):
    """
        Arguments:
                filename: the name of the file to write into
                text: what to write into the file

        Return: the number of character written
    """

    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
