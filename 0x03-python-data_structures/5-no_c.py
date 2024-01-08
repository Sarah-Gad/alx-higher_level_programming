#!/usr/bin/env python3
def no_c(my_string):
    if my_string is None:
        my_string = ""
    else:
        convrtd = list(my_string)
        thelen = len(convrtd)
        i = thelen - 1
        while i >= 0:
            if convrtd[i] == "c" or convrtd[i] == "C":
                convrtd.pop(i)
            i -= 1
        return ("".join(convrtd))
