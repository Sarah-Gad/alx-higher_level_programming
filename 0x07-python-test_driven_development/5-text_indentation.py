#!/usr/bin/python3
"""This module contains text_indentation method."""


def text_indentation(text):
    """This method is adding 2 new lines after '.?:' chars.

    Args:
        text: The actual txt
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
