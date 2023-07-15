#!/usr/bin/python3
""" A module that convert json to python """
import json


def from_json_string(my_str):
    """My convert to python function

    Args:
            my_str: a string in json

    Return:
            the python representation of jason
    """
    return json.loads(my_str)
