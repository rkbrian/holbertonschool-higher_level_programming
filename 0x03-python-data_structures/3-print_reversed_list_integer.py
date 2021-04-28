#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    newly = my_list[::-1]
    for i in newly:
        print("{:d}".format(i))
