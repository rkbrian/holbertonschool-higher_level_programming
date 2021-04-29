#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Keanu = [[]]
    for i in range(len(matrix)):
        Keanu[i] = list(map(lambda j : j ** 2, matrix[i]))
    return Keanu
