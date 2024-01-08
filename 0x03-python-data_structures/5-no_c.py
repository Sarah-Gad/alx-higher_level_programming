#!/usr/bin/env python3
def no_c(my_string):
    if my_string is None:
        my_string = ""
    else:
        convrtd = list(my_string)
        thelen = len(convrtd)
        nwstr = []
        for i in range(thelen):
            if convrtd[i] != "c" and convrtd[i] != "C":
                nwstr.append(convrtd[i])
        return ("".join(nwstr))
