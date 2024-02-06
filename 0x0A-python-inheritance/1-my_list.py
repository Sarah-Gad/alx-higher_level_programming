#!/usr/bin/python3


"""Class MyList that inheritslist"""


class MyList(list):
    """Class MyList that inheritslist"""

    def print_sorted(self):
        """Print the sorted list"""

        sorted_l = sorted(self)
        print(sorted_l)
