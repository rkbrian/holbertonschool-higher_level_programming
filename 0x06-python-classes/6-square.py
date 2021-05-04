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

    @property
    def position(self):
        """getter to retrieve position"""
        return self.__position

    @size.setter
    def size(self, value):
        """setter to set size value"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter to set position"""
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) == 2 and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """initialize objects"""
        self.__size = size
        self.__position = position

    def area(self):
        """area calculation"""
        return (self.__size ** 2)

    def my_print(self):
        """hashtag matrix printing"""
        if self.__size == 0:
            print()
        else:
            for i in range(1, self.__position[1] + 1):
                print()
            for j in range(self.__size):
                print("{}".format(" ") * self.__position[0], end="")
                print("{}".format("#") * self.__size, end="")
                print()
