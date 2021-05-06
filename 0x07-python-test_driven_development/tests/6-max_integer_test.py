#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer()"""
    def testthemaxinteger(self):
        """function to test the max int"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

if __name__ == "__main__":
    """execute the main inputs"""

    unittest.main()
