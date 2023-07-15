#!/usr/bin/python3
""" A module that that retuens a JSON rep of an obj """
import json


def to_json_string(my_obj):
    """My json comverter function

    Args:
        my_obj: a python string

    Return:
            the json representation of python
    """
    return json.dumps(my_obj)
