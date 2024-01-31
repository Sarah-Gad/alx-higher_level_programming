#!/usr/bin/python3
"""This mofule defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass
    """

    __slots__ = ["first_name"]
