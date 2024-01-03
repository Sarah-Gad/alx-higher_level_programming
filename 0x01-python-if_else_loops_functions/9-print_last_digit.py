#!/usr/bin/python3
def print_last_digit(number):
    lst_num = abs(number) % 10
    print("{:d}" .format(lst_num), end="")
    return lst_num
