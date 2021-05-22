#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
Rectangle = __import__('model.rectangle').Rectangle

class Tesseract(unittest.TestCase):
    """unittest class for max_integer()"""
    def testthemaxinteger(self):
        """function to test the max int"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    """execute the main inputs"""

    unittest.main()
