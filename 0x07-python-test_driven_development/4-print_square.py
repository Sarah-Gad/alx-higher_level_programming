#!/usr/bin/python3
"""This module contains print_square method."""


def print_square(size):
    """Method is  printing a square with # characters.

    Args:
        size: the size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
