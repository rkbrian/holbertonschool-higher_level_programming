#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delist = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            delist.append(k)
    [a_dictionary.pop(k) for k in delist]
    return a_dictionary
