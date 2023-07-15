#!/usr/bin/python3
""" A module that writes an Obj to a txt, using a JSON rep """
import json


def save_to_json_file(my_obj, filename):
    """ My json function

    Args:
        my_obj: a string of a python obj to be converted to json
        filename: the file where the converted string would be stored
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
