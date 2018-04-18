#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for t in range(len(matrix[i])):
            if t < len(matrix[i]):
                print("{:d}".format(matrix[i][t]), end=" ")
            else:
                print("{:d}".format(matrix[i][t]))
        print()
