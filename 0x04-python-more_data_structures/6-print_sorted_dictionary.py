#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mylist = list(a_dictionary.items())
    mylist.sort()
    for key, value in mylist:
        print("{:s}: {}" .format(key, value))
