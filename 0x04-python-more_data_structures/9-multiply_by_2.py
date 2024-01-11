#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dict = {}
    for key, value in a_dictionary.items():
        nw_dict[key] = (value * 2)
    return nw_dict
