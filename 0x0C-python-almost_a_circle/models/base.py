#!/usr/bin/python3
"""module for class Base"""



class Base:
    """base class for unittest projects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
