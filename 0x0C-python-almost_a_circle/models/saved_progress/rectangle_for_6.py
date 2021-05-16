#!/usr/bin/python3
"""module for class rectangle"""


from models.base import Base


class Rectangle(Base):
    """class that inherits class Base"""

    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def integer_validator(self, attr, value):
        """integer validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))
        if (attr == 'width' and value <= 0):
            raise ValueError("{} must be > 0".format(attr))
        if (attr == 'height' and value <= 0):
            raise ValueError("{} must be > 0".format(attr))
        if (attr == "x" and value < 0) or (attr == "y" and value < 0):
            raise ValueError("{} must be >= 0".format(attr))

    def area(self):
        """the area method implementation"""
        return (self.__width * self.__height)

    def display(self):
        """visualize the rectangle"""
        hashmatrix = ""
        for i in range(self.__height - 1):
            hashmatrix += "{}".format(self.print_symbol) * self.__width
            hashmatrix += "\n"
        hashmatrix += "{}".format(self.print_symbol) * self.__width
        print(hashmatrix)

    def __str__(self):
        """return rectangle id"""
        str1 = "({}) {}/{}".format(self.id, self.__x, self.__y)
        str2 = " - {}/{}".format(self.__width, self.__height)
        return "[Rectangle] " + str1 + str2

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """width setter"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.integer_validator("y", value)
        self.__y = value
