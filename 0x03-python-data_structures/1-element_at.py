#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    thelen = len(my_list) - 1
    if idx > thelen:
        return None
    else:
        thevalue = my_list[idx]
        return thevalue
