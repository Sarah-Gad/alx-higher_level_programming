#!/usr/bin/python3
def multiple_returns(sentence):
    thelen = len(sentence)
    if sentence is None:
        first = None
    else:
        first = sentence[0]
    returned_t = (thelen, first)
    return returned_t
