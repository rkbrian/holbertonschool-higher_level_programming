#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for ch in my_string:
        if ch != "c" and ch != "C":
            newstr += ch
    return newstr
