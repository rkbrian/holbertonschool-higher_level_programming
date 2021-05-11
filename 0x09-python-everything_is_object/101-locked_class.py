#!/usr/bin/python3
"""class LockedClass: module for a locked class
"""


class LockedClass:
    """A class that prevents the user from dynamically creating
    new instance attributes.
    """

    __slots__ = "first_name"
