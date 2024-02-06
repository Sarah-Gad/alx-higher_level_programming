#!/usr/bin/python3
""" this module contains file manibulation"""


def save_to_json_file(my_obj, filename):
    """This method writes an object to a text file"""
    import json
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
