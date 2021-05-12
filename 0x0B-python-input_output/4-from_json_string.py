#!/usr/bin/python3
"""module for function from_json_string"""


def from_json_string(my_str):
    """function to return the Python format of he given JSON format str"""

    import json
    JasonBourneID = json.loads(my_str)
    return JasonBourneID
