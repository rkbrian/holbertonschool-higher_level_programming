#!/usr/bin/python3
"""
module to return True or False for class judgment
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class: function to return if it is the instance's type or
    inherited type"""

    return (isinstance(obj, a_class))
