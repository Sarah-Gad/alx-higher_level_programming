#!/usr/bin/python3/
"""This module usues json strings"""
import json


def class_to_json(obj):
    """This method returns a dictionary
    description with simple data structure"""
    mydict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            mydict[key] = value
    return mydict
