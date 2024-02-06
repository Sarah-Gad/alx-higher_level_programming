#!/usr/bin/python3


"""Class MyList that inherits list"""


class MyList(list):
    """Class MyList that inherits  list"""

    def print_sorted(self):
        """Print the sorted list"""

        sorted_l = sorted(self)
        print(sorted_l)
