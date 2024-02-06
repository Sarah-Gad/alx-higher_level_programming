#!/usr/bin/python3
"""This module handles data heirarchy"""


def to_json_string(my_obj):
    """This module returns the json representaion of an object"""
    import json
    conv = json.dumps(my_obj)
    return conv
