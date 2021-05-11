#!/usr/bin/python3
"""
module to return True or False for class judgment
"""


def is_same_class(obj, a_class):
    """is_name_class: function to return if it is the instance's class"""

    return (type(obj) is a_class)
