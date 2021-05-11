#!/usr/bin/python3
"""
module for BaseGeometry, the class with some functions in it
"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
