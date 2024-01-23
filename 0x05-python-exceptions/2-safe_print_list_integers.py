#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    num_p = 0
    while idx < x:
        if (isinstance(my_list[idx], int)):
            try:
                print("{:d}".format(my_list[idx]), end="")
                num_p += 1
            except IndexError:
                raise
        idx += 1
    print()
    return num_p
