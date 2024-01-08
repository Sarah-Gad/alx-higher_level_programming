#!/usr/bin/env python3
def no_c(my_string):
    nwlst = list(my_string)
    i = 0
    while i < len(nwlst):
        if nwlst[i] == 'c' or nwlst[i] == 'C':
            nwlst.pop(i)
        else:
            i += 1
    return (''.join(nwlst))
