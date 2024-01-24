#!/usr/bin/python3
"""This is a definition of a class square"""


class Square:
    """the code inside the class"""
    def __init__(self, size=0, position=(0, 0)):
        """This is the constuctor function, instance.

        Args:
        size(int): the acual size of the square.
        position(int, int): the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ a method to be able to retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ a method to ba able to edit the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0:")
        self.__size = value

    @property
    def position(self):
        """ a method to retrieve the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ a method to set the value of position"""
        if not isinstance(value, tuple) or \
                len(value) != 2 or not \
                all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError(
                            "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ This is instance method that reterns
        the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.size == 0:
            print()
            return
        for s in range(self.position[1]):
            print()
        for a in range(self.size):
            for r in range(self.position[0]):
                print(" ", end="")
            for h in range(self.size):
                print("#", end="")
            print()
