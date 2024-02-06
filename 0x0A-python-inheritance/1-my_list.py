#!/usr/bin/python3


"""This is a module for MyList"""


class MyList(list):
    """This is MyList class"""
    def print_sorted(self):
        """The method for printing"""
        print(sorted(self))
