#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = my_list.copy()
    for i in nw_list:
        if i == search:
            theind = my_list.index(i)
            my_list.pop(theind)
            my_list.insert(theind, replace)
    return nw_list
