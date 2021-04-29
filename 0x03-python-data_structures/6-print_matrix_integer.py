#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for i in range(len(matrix)):
            print("{:d}".format(matrix[i][0]), end="")
            for j in range(1, len(matrix[i])):
                print(" {:d}".format(matrix[i][j]), end="")
            print("")
