#!/usr/bin/python3
"""
module for lookup that returns the list
of available attributes and methods of an object
"""


def lookup(obj):
    """lookup: function to return object directory"""

    return dir(obj)
