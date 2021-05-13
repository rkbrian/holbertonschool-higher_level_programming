#!/usr/bin/python3
"""module for class Student, the class of info of students"""


class Student:
    """including first name, last name, age"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieving dictionary representation"""
        return self.__dict__
