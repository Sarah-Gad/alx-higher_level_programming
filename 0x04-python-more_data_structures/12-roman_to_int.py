#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_v = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    tot = 0
    prev_v = 0

    for sym in reversed(roman_string):
        value_r = roman_v[sym]
        if value_r >= prev_v:
            tot += value_r
        else:
            tot -= value_r
            prev_v = value_r

    return tot
