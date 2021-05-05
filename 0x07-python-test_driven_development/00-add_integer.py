#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        return int(a + b)
    except:
        if type(a) != int and type(a) != float:
            return ("a must be an integer")
        if type(b) != int and type(a) != float:
            return ("b must be an integer")
