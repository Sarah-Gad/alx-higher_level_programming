#!/usr/bin/python3
"""This module is for defining a Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """This rectangle class is the child class of the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """this method returns the area value of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Tjis method prints the rectangle"""
        for s in range(self.y):
            print("")
        for i in range(self.height):
            for h in range(self.x):
                print(" ", end="")
            for z in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """returns the string representaion of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """This method assigns an argument to each attribute"""
        if (len(args) != 0):
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        elif (len(kwargs) != 0):
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "width":
                    self.width = val
                if key == "height":
                    self.height = val
                if key == "x":
                    self.x = val
                if key == "y":
                    self.y = val

    def to_dictionary(self):
        """ a method to return a dictionary representation"""
        dicty = {}
        dicty["id"] = self.id
        dicty["width"] = self.width
        dicty["height"] = self.height
        dicty["x"] = self.x
        dicty["y"] = self.y
        return dicty
