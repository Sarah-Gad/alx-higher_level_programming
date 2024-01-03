#!/usr/bin/python3
def uppercase(str):
    up_string = ""
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            up_char = chr(ord(char) - 32)
            up_string += up_char
        else:
            up_string += char
    print("{}".format(up_string))
