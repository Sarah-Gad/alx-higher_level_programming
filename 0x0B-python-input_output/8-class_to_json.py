#!/usr/bin/python3/
"""This module usues json strings"""
import json


def class_to_json(obj):
    """This method returns a dictionary
    description with simple data structure"""
    return obj.__dict__
