#!/usr/bin/python3
""" This module defines a class Base """
import json


class Base:
    """ The Base of all other classes to be created """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize id Field """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A static method that returns json representation of duct"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the json string in a file """
        fptr = cls.__name__ + '.json'
        with open(fptr, 'w', encoding='utf-8') as my_file:
            if not list_objs:
                lst = []
            else:
                lst = [att.to_dictionary() for att in list_objs]
            my_file.write(Base.to_json_string(lst))
