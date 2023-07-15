#!/usr/bin/python3
""" A module that converts json to python from a file """
import json


def load_from_json_file(filename):
    """ My function that converts json to python

    Args:
        filename: the name containing the json str
    
    Return:
            The python form of json
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.loads(my_file.read())
