#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    newly = reversed(my_list)
    for i in newly:
        print("{:d}".format(i))
