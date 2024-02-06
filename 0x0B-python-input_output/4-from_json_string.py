#!/usr/bin/python3
""" this module handles some data heirarchies"""


def from_json_string(my_str):
    """This module returns an object represented by json string"""
    import json
    conv = json.loads(my_str)
    return conv
