#!/usr/bin/python3
"""module for function write_file"""


def write_file(filename="", text=""):
    """function to write some texts to the given file name"""

    with open(filename, mode="w", encoding="utf-8") as Writethis:
        return Writethis.write("{}".format(text))
