#!/usr/bin/python3
"""module for class rectangle"""


from models.base import Base
import inspect


class Rectangle(Base):
    """class that inherits class Base"""

    symb = "#"
    orderarg = ["id", "width", "height", "x", "y"]

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
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            hashy = "\n" * self.__y
            xspace = " " * self.__x
            for i in range(self.__height - 1):
                hashy += xspace + "{}".format(self.symb) * self.__width
                hashy += "\n"
            hashy += xspace + "{}".format(self.symb) * self.__width
            print(hashy)

    def __str__(self):
        """return rectangle id"""
        str1 = "({}) {}/{}".format(self.id, self.__x, self.__y)
        str2 = " - {}/{}".format(self.__width, self.__height)
        return "[Rectangle] " + str1 + str2

    def update(self, *args, **kwargs):
        """assign arguments to each attribute"""
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, orderarg[i], args[i])
        else:
            for j in kwargs:
                if hasattr(self, j) is True:
                    setattr(self, j, kwargs[j])

    def to_dictionary(self):
        """return the dictionary representation of Rectangle"""
        rec_dict = {}
        rec_dict[self.orderarg[0]] = self.id
        rec_dict[self.orderarg[1]] = self.width
        rec_dict[self.orderarg[2]] = self.height
        rec_dict[self.orderarg[3]] = self.x
        rec_dict[self.orderarg[4]] = self.y
        return rec_dict

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
