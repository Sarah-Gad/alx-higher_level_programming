#!/usr/bin/python3
mynums = list(range(99))
for pro in mynums:
    des_num = int(pro)
    hex_num = hex(pro)
    print("{:d} = {:s}" .format(des_num, hex_num))
