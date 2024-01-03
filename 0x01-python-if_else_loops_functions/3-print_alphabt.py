#!/usr/bin/python3
alpha = "abcdefghijklmnopqrstuvwxyz"
for progress in alpha:
    if progress == "q" or progress == "e":
        continue
    print("{:s}" .format(progress), end="")
