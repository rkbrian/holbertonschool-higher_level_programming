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

    try:
        return int(a + b)
    except:
        if type(a) != int and type(a) != float:
            raise TypeError("a must be an integer")
        if type(b) != int and type(a) != float:
            raise TypeError("b must be an integer")
