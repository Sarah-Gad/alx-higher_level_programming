#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_p = 0
    idx = 0
    try:
        while idx < x:
            print(f"{my_list[idx]}", end="")
            num_p += 1
            idx += 1
    except IndexError:
        pass
    finally:
        print()
        return num_p
