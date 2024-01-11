#!/usr/bin/python3
def complex_delete(a_dictionary, thevalue):
    if not isinstance(a_dictionary, dict):
        return None
    for thekey, theval in tuple(a_dictionary.items()):
        if theval == thevalue:
            del a_dictionary[thekey]
    return a_dictionary
