#!/usr/bin/python3
"""module for class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class instructor"""
        super().integer_validator("width", size)
        super().integer_validator("height", size)
        self.__width = size
        self.__height = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return square id"""
        str1 = "({}) {}/{}".format(self.id, self.x, self.y)
        str2 = " - {}".format(self.__width)
        return "[Square] " + str1 + str2

    def update(self, *args, **kwargs):
        """assign arguments to each attribute"""
        if args and len(args) > 0:
            orderarg = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, orderarg[i], args[i])
        else:
            for j in kwargs:
                if hasattr(self, j) is True:
                    setattr(self, j, kwargs[j])

    def to_dictionary(self):
        """return the dictionary representation of Square"""
        rec_dict = {}
        rec_dict["id"] = self.id
        rec_dict["size"] = self.width
        rec_dict["x"] = self.x
        rec_dict["y"] = self.y
        return rec_dict

    @property
    def size(self):
        """getter for size"""
        return self.__width

    @size.setter
    def size(self, value):
        """size setter"""
        self.integer_validator("width", value)
        self.__width = value
        self.__height = value
