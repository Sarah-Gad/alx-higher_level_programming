#!/usr/bin/python3
"""This module define a square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class is a child of the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = val

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """a method that assigns the attributes"""
        if (len(args) != 0):
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = self.height = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1

        elif (len(kwargs) != 0):
            for k, v in kwargs.items():
                if k == "size":
                    self.width = self.height = v
                if k == "id":
                    self.id = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
