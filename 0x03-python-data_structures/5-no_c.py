#!/usr/bin/env python3
def no_c(my_string):
    nwstr = ""
    for i in my_string:
        if i.lower() not in {'c'}:
            nwstr = nwstr + i
    return nwstr
