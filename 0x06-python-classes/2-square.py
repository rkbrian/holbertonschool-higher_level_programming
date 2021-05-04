#!/usr/bin/python3
""" class Square: contains private instance attribute (size) with err msg """


class Square:
    """ def and initiate size, manage output, no type preference, raise err """

    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
