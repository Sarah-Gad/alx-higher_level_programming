#!/usr/bin/python3
"""This module define find peak method"""


def find_peak(list_of_integers):
    """this mehtod will  return the peak in a list of ints"""
    if list_of_integers == []:
        return None
    list_size = len(list_of_integers)
    if list_size == 1:
        return list_of_integers[0]
    elif list_size == 2:
        return max(list_of_integers)
    middle_element = int(list_size / 2)
    its_apeak = list_of_integers[middle_element]
    if its_apeak > list_of_integers[middle_element - 1] and\
            its_apeak > list_of_integers[middle_element + 1]:
        return its_apeak
    elif its_apeak < list_of_integers[middle_element - 1]:
        return find_peak(list_of_integers[:middle_element])
    else:
        return find_peak(list_of_integers[middle_element + 1:])
