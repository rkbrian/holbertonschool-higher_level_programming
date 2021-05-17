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
        import json
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
        """note to myself:
        since the 1st obj (id) is always 1, I need to
        differenciate Rectangle and Square by changing the 2nd obj
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1, 2)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy
