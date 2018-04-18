#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(matrix.shape[0]):
        for t in range(matrix.shape[1]):
            print("{:d}".format(matrix), if t == matrix.shape[1] else end=" ")
