#!/usr/bin/env python3
def no_c(my_string):
    if my_string is None:
        my_string = ""
    else:
        nwstr = ""
        for i in my_string:
            if i.lower() not in {'c'}:
                nwstr = nwstr + i
        return nwstr
