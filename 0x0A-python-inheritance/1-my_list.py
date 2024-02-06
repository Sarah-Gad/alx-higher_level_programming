#!/usr/bin/python3


"""Class MyList that inherits from list"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Print the sorted list"""

        sorted_l = sorted(self)
        print(sorted_l)
