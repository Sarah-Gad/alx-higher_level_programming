#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        thelen = len(my_list)
        big = my_list[0]
        for i in range(1, thelen):
            if big < my_list[i]:
                big = my_list[i]
        return big
