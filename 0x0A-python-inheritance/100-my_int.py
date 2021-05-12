#!/usr/bin/python3
"""
module for class MyInt
"""


class MyInt(int):
    """functions to show the opposite Boolean value"""

    def __eq__(self, other):
        """excluded number"""
        return int(self) is not int(other)

    def __ne__(self, other):
        """set the opposed target"""
        return int(self) is int(other)
