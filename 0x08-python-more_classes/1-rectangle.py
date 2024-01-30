#!/usr/bin/python3
""" This class defines a rectangle"""


class Rectangle:
    """ This is the code inside the class"""
    def __init__(self, width=0, height=0):
        """ the will create objects withe the attributes
        Args:
        width(int): the withe of the rectangle.
        height(int): the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This will retrive the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ this will set a value to the width attribute"""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if (self.__width < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This will retieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This will set the value of height"""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if (self.__height < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
