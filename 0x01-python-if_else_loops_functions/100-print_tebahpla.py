#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        alpha = chr(i).lower()
    else:
        alpha = chr(i).upper()
     print("{}".format(alpha), end="")
