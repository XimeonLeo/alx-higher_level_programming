#!/usr/bin/python3
""" My list inheritance """


class MyList(list):
    """ a sub-class inherited from list a super class """

    def print_sorted(self):
        """ Prints a list in ascending order """
        print(sorted(self))
