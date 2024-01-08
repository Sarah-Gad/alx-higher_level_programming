#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        thelen = len(sentence)
        first = "None"
        returned = (thelen, first)
        return returned
    else:
        thelen = len(sentence)
        first = sentence[0]
        returned_t = (thelen, first)
        return returned_t
