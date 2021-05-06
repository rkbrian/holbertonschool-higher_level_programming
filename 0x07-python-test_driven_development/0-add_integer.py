#!/usr/bin/python3
"""
    add_integer: the module
    a: the first input
    b: the second input
"""


def add_integer(a, b=98):
    """
        a is the 1st value and b is the second, return the sum
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
