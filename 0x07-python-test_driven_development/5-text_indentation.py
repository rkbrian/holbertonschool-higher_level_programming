#!/usr/bin/python3
"""
text_indentation: text indentation
"""


def text_indentation(text):
    """print new lines"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        cutter = ".?:"
        for i in range(len(text)):
            if not text[i - 1] in cutter:
                print("{}".format(text[i]), end="")
            else:
                print("{}".format("\n"))
