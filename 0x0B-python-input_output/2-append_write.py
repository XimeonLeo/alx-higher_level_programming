#!/usr/bin/python3
""" A module that appends into a file """


def append_write(filename="", text=""):
    """
        Arguments:
                filename: the name of the file to append to
                text: what to writ into the file

        Return: the number of files written
    """

    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
