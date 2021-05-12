#!/usr/bin/python3
"""module for function append_write"""


def append_write(filename="", text=""):
    """"""

    with open(filename, mode="a", encoding="utf-8") as Appendthis:
        Appendthis.write(text)
