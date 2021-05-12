#!/usr/bin/python3
"""
module for class MyInt
"""


class MyInt(int):
    """functions to show the opposite Boolean value"""

    def __init__(self, number):
        """initializing the input number"""
        self.number = number

    def __eq__(self, exnum):
        """excluded number"""
        return self.number == exnum.number

    def __ne__(self, exnum):
        """3 as the opposed target"""
            return not self.__eq__(exnum)
