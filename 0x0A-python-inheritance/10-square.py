#!/usr/bin/python3
"""
module for Square, the class with some functions in it
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """the area method implementation"""
        return (self.__size * self.__size)
