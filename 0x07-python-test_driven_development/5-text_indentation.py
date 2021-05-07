#!/usr/bin/python3
"""
text_indentation: text indentation
"""


def text_indentation(text):
    """print new lines"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        newtext = text
        cutter = ".?:"
        for j in range(len(text)):
            newtext = newtext.replace(". ", ".", 1)
            newtext = newtext.replace("? ", "?", 1)
            newtext = newtext.replace(": ", ":", 1)
        for i in range(len(newtext)):
            if not newtext[i - 1] in cutter:
                print("{}".format(newtext[i]), end="")
            else:
                print("\n\n{}".format(newtext[i]), end="")
