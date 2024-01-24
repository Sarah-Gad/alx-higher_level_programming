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
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ a method to retrieve the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ a method to set the value of position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
        not all(isinstance(first, int) for first in value) or
        not all(second >= 0 for second in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ This is instance method that reterns
        the current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """ a method to prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for s in range(self.__size):
                    print("#", end="")
                print()

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
