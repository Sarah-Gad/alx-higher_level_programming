#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for idx in range(1, 3):
        try:
            if idx > a:
                raise Exception('Too far')
            else:
                res += a ** b / idx
        except Exception:
            res = b + a
            break
    return result
