#!/usr/bin/python3
""" This class defines a rectangle"""


class Rectangle:
    """ This is the code inside the class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ the will create objects withe the attributes
        Args:i
        width(int): the withe of the rectangle.
        height(int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This will retrive the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ this will set a value to the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This will retieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This will set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """a method to return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """a method to retuen the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ a method to return the shape of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        else:
            shape = []
            for i in range(self.__height):
                for s in range(self.__width):
                    shape.append(Rectangle.print_symbol)
                if i != self.__height - 1:
                    shape.append("\n")
            return ("".join(shape))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
