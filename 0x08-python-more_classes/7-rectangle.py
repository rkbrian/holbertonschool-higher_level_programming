#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initiation with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                hashmatrix += "{}".format(self.print_symbol) * self.__width
                hashmatrix += "\n"
            hashmatrix += "{}".format(self.print_symbol) * self.__width
            return hashmatrix

    def __repr__(self):
        """recreating new instance with eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """action while deleting the imported class: print message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
