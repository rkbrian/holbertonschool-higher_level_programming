#!/usr/bin/python3
"""
class Locked_Class
"""


class Locked_Class:
    """
    Class to prevents the user from dynamically creating
    new instance attributes.
    """

    __slots__ = "first_name"
