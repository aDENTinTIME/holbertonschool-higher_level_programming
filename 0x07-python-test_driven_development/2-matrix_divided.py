#!/usr/bin/python3
"""2-matrix_divided
Attributes:
    matrix: Matrix of numbers.
    div: Number to divide matrix by.
"""


def matrix_divided(matrix, div):
    """matrix_divided
    Divides the contents of a matrix by div.
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    length = len(matrix[0])
    for i in matrix:
        hold = []
        if length != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for t in i:
            if not isinstance(t, int) and not isinstance(t, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of"
                    + " integers/floats")
            hold.append(round(t/div, 2))
        new_matrix.append(hold)
    return new_matrix
