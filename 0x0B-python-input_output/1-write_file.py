#!/usr/bin/python3
""" This module contains a method to handle a file"""


def write_file(filename="", text=""):
    """This method or function oens a file and writes into it"""
    with open(filename, 'w', encoding="utf-8") as myfile:
        numwritten = myfile.write(text)
        return numwritten
