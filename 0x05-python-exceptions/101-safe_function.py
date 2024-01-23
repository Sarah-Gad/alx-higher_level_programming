#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except BaseException as excep:
        print("Exception: {}".format(excep), file=stderr)
        return None
