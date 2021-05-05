#!/usr/bin/python3
"""
    matrix_divided: the module
    matrix: the dividend matrix
    div: the divisor
"""


def matrix_divided(matrix, div):
    """
        return the divided matrix
    """

    try:
        Keanu = [list(map(lambda j: round(j / div, 2), Neo)) for Neo in matrix]
        return Keanu
    except:
        if type(k) != int and type(k) != float for k in matrix:
            raise TypeError("Each row of the matrix must have the same size")
        if len(matrix[i]) != len(matrix[0]) for i in range(len(matrix)):
            raise TypeError("Each row of the matrix must have the same size")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if type(div) != int and type(div) != float
            raise TypeError("div must be a number")
