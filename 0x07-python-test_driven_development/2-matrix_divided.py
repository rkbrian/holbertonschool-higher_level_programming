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

    for k in range(len(matrix)):
        for l in range(len(matrix[k])):
            if type(matrix[k][l]) != int and type(matrix[k][l]) != float:
                raise TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[k]) != len(matrix[0]):
            raise TypeError
            ("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    Keanu = [list(map(lambda j: round(j / div, 2), Neo)) for Neo in matrix]
    return Keanu
