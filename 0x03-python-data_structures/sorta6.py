#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for t in i:
            if t < len(i):
                print("{:d}".format(t), end=" ")
            else:
                print("{:d}".format(t))
