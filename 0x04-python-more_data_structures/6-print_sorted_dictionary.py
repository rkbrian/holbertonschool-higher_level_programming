#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for strings in sorted(a_dictionary):
        print("{0}: {1}".format(strings, a_dictionary[strings]))
