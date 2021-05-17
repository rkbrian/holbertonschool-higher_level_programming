#!/usr/bin/python3
"""module for class Base"""


import json


class Base:
    """base class for unittest projects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to return JSON str rep"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """static method to return str from JSON str"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method to write JSON str rep"""
        with open(cls.__name__ + ".json", mode="w") as JasonBourne:
            Jason = []
            if list_objs:
                for c in list_objs:
                    Jason.append(cls.to_dictionary(c))
            JasonBourne.write(Base.to_json_string(Jason))

    @classmethod
    def create(cls, **dictionary):
        """class method to return an instance with all attr set"""
        """Note to myself:
        since the 1st obj (id) is always 1, I need to
        differenciate Rectangle and Square by changing the 2nd obj
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances from content of json file"""
        """Note to myself: the procedures
        capture json string from json file and convert it;
        making dictionaries for all the instances in the converted;
        distribute instance from dictionaries to the class for update
        """
        from os import path
        fname = cls.__name__ + ".json"
        if path.exists(fname) is False:
            return []
        else:
            with open(fname, mode="r") as JasonBorn:
                json_str = JasonBorn.read()
                reg_str = cls.from_json_string(json_str)
            if cls:
                linst = []
                for x in reg_str:
                    new_dict = dict(x)
                    linst.append(cls.create(**new_dict))
            return linst
