#!/usr/bin/python3
"""
module for Rectangle, the class with some functions in it
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """the area method implementation"""
        return (self.__width * self.__height)

    def __str__(self):
        """return to the Rectangle info to print"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
