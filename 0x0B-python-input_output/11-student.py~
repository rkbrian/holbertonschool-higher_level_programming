#!/usr/bin/python3
"""module for class Student, the class of info of students"""


class Student:
    """including first name, last name, age"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieving dictionary representation"""
        dictcopy = self.__dict__.copy()
        xliteral = {}
        if type(attrs) == list:
            for j in dictcopy:
                for i in range(len(attrs)):
                    if j == attrs[i]:
                        xliteral[j] = dictcopy[j]
            return xliteral
        return self.__dict__
