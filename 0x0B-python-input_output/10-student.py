#!/usr/bin/python3
"""This module defines a student class"""


class Student:
    """ This is a class that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a method that retrieves a dictionary
        representation of a Student instance"""
        mydict = {}
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            for key, value in self.__dict__.items():
                if key in attrs:
                    mydict[key] = value
        return mydict
