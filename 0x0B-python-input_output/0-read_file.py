#!/usr/bin/python3
"""module for function read_file"""


def read_file(filename=""):
    """function to write some texts in the given file name"""

    import os
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write("Holberton School offers a truly innovative approach to \
education:\nfocus on building reliable applications and scalable \
systems, take on real-world challenges, collaborate with your \
peers. \n\nA school every software engineer would have dreamt of!\n")