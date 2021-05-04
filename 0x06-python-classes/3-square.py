#!/usr/bin/python3
""" class Square: contains the following items:
    size: private instance attribute
    TypeError: type error messages
    ValueError: value error messages
    area: public instance method
"""


class Square:
    """ def and initiate size, manage output, no type preference, raise err """

    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
