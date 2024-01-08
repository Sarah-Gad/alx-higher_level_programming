#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list.copy())
    thelen = len(my_list) - 1
    if idx > thelen:
        return (my_list.copy())
    else:
        nwlist = my_list.copy()
        nwlist[idx] = element
        return nwlist
