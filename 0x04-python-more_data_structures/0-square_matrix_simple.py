#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        hold = []
        for t in i:
            hold.append(t**2)
        new_matrix.append(hold)
    return new_matrix
