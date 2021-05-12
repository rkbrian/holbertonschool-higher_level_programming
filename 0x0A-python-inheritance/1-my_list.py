#!/usr/bin/python3
"""
module for class Mylist that inherits from list
"""


class MyList(list):
    """the class to inherit list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
