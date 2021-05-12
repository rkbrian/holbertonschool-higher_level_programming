#!/usr/bin/python3
"""module for function to_json_string"""


def to_json_string(my_obj):
    """function to return the JSON format of he given object"""

    import json
    JasonBourne = json.dumps(my_obj)
    return JasonBourne
