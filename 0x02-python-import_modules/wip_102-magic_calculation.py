#!/usr/bin/python3
from magic_calculation_102 import add sub

def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
