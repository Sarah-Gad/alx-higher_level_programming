#!/usr/bin/python3
first = list(range(10))
for pro_f in first:
    second = list(range(pro_f + 1, 10))
    for pro_s in second:
        if pro_f == 8 and pro_s == 9:
            print("{:d}{:d}".format(pro_f, pro_s))
        else:
            print("{:d}{:d}, " .format(pro_f, pro_s), end="")
