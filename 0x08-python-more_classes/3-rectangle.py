#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        """initiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area calculation"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter calculation"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """visualizing hashtag string output"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            hashmatrix = ""
            for i in range(self.__height - 1):
                hashmatrix += "#" * self.__width + "\n"
            hashmatrix += "#" * self.__width
            return hashmatrix
