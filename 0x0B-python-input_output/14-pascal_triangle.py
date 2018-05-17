#!/usr/bin/python3


def pascal_triangle(n):
    tri = []
    hold = []
    for x in range(1, n):
        for y in range(1, x):
            hold.append(y)
        tri.append(hold)
    return tri
"""
    return [[1],[1,1],[1,2,1]]
        tri[0] = x
        tri[-1] = x
        tri[x-1] = x
"""
