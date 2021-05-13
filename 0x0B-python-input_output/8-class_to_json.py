#!/usr/bin/python3
"""module for class_to_json"""


def class_to_json(obj):
    """function to return dict description with simple data struct"""

    return obj.__dict__
