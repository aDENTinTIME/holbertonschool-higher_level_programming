#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    for i in matrix:
        hold = []
        for t in i:
            hold.append(int(t/div*100)/100)
        new_matrix.append(hold)
    return new_matrix
