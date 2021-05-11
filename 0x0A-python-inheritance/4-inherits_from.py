#!/usr/bin/python3
"""
module to return True or False for class inheritance judgment
"""


def inherits_from(obj, a_class):
    """inherited_from: function to return if the instance is inherited"""

    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
