#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = my_list.copy()
    for i in nw_list:
        if i == search:
            theind = nw_list.index(i)
            nw_list.pop(theind)
            nw_list.insert(theind, replace)
    return nw_list
