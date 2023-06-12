#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        length = len(my_list)
        for elem in range(length - 1, -1, -1):
            print("{:d}".format(my_list[elem]))
