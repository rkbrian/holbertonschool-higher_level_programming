#!/usr/bin/python
"""module for function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function to insert a text line to a file"""

    writeall = ""
    with open(filename, mode="r") as Cut_in_line:
        readall = Cut_in_line.readline()
        while readall:
            if search_string in readall:
                writeall += readall + new_string
            else:
                writeall += readall
            readall = Cut_in_line.readline()
    with open(filename, mode="w") as Cut_in_line:
        Cut_in_line.write(writeall)
