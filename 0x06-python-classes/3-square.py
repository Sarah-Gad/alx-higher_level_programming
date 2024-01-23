#!/usr/bin/python3
"""This is a definition of a class square"""


class Square:
    """the code inside the class"""
    def __init__(self, size=0):
        """This is the constuctor function, instance.

        Args:
        size(int): the acual size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ This is instance method that reterns
        the current square area.
        """
        return self.__size * self.__size
