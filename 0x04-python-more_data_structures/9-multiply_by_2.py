#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for stuff in a_dictionary:
        a_dictionary[stuff] = a_dictionary[stuff] * 2
    return a_dictionary
