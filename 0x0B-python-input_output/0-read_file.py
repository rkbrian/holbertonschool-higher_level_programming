#!/usr/bin/python3
"""module for function read_file"""


def read_file(filename=""):
    """function to read some texts in the given file name"""

    with open(filename) as Readthis:
        print(Readthis.read(), end="")
