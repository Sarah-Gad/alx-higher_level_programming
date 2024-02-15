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

    @staticmethod
    def from_json_string(json_string):
        """ This method returns the list of the JSON str"""
        if json_string is None or not json_string:
            return []
        else:
            thelist = json.loads(json_string)
            return thelist

    @classmethod
    def create(cls, **dictionary):
        """a emthod that returns an instance with all attributes already set"""
        if dictionary and dictionary is not None:
            if cls.__name__ == "Rectangle":
                dummy = cls(5, 6)
            else:
                dummy = cls(8)
            dummy.update(**dictionary)
            return dummy
