#!/usr/bin/python3
""" this module manipulates  a file"""


def load_from_json_file(filename):
    """This method creates an Object from a “JSON file”"""
    import json
    with open(filename, 'r') as myfile:
        ret = json.load(myfile)
        return ret
        
