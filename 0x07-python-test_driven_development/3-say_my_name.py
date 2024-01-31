#!/usr/bin/python3
"""This modue;l contains say_my_name method."""


def say_my_name(first_name, last_name=""):
    """Method for printing first and last name.

    Args:
        first_name: the first
        last_name: the second
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
