#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if len(matrix[i]) > 0:
            for j in range(len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]), end=" ")
            print("{:d}".format(matrix[i][j + 1]))
        else:
            print("{}".format(""))
