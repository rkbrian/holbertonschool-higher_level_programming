#!/usr/bin/python3
""" class Square: contains the following items:
    size: private instance attribute
    TypeError: type error messages
    ValueError: value error messages
    area: public instance method
"""


class Square:
    """ def and initiate size, manage output, no type preference, raise err """

    @property
    def size(self):
        """getter to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter to set size value"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __init__(self, size=0):
        """initialize objects"""
        self.__size = size

    def area(self):
        """area calculation"""
        return (self.__size ** 2)
