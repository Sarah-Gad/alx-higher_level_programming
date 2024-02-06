#!/usr/bin/python3
""" this module handles a file"""


def append_write(filename="", text=""):
    """This methods opens a file and add text to it"""
    with open(filename, 'a', encoding="utf-8") as myfile:
        numwritten = myfile.write(text)
        return numwritten
