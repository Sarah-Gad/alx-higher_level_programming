#!/usr/bin/python3
"""This module conyains a function of method to read from a file"""


def read_file(filename=""):
    """The method to read and print"""
    with open(filename, 'r', encoding="utf-8") as myfile:
        read = myfile.read()
        print(read, end="")
