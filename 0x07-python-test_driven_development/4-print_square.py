#!/usr/bin/python3
"""
print_square: function to print a square
"""


def print_square(size):
    """input size"""

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
