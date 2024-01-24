#!/usr/bin/python3
"""This is a definition of a class square"""


class Square:
    """the code inside the class"""
    def __init__(self, size=0):
        """This is the constuctor function, instance.

        Args:
        size(int): the acual size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """ a method to be able to retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ a method to ba able to edit the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0:")
        else:
            self.__size = value

    def area(self):
        """ This is instance method that reterns
        the current square area.
        """
        return self.__size * self.__size
