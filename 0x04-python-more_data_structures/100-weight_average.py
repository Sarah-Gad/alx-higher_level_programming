#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    wts = sum(map(lambda t: t[0] * t[1], my_list))
    divis = sum(map(lambda t: t[1], my_list))
    return wts / divis
