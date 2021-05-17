#!/usr/bin/python3
"""module for class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class instructor"""
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return square id"""
        str1 = "({}) {}/{}".format(self.id, self.x, self.y)
        str2 = " - {}".format(self.__width)
        return "[Square] " + str1 + str2
