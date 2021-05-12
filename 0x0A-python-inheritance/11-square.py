#!/usr/bin/python3
"""
module for Square, the class with some functions in it
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)

    def area(self):
        """the area method implementation"""
        return (self.__size * self.__size)

    def __str__(self):
        """return the Square info to print"""
        return ("[Square]{}/{}".format(self.__size, self.__size))
