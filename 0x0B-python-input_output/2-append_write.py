#!/usr/bin/python3
"""module for function append_write"""


def append_write(filename="", text=""):
    """function to append some texts to the given file name"""

    with open(filename, mode="a", encoding="utf-8") as Appendthis:
        return Appendthis.write("{}".format(text))
