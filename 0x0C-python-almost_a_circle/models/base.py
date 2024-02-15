#!/usr/bin/python3
"""This module contain the base class"""

import json


class Base:
    """This class manages id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ amethod that writes the JSON string
        representation of list_objs to a file"""
        name = cls.__name__ + ".json"
        with open(name, 'w') as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                listofdic = [ob.to_dictionary() for ob in list_objs]
                myfile.write(Base.to_json_string(listofdic))
