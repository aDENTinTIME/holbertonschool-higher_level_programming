#!/usr/bin/python3
"""0-add_integer
Attributes:
    a: First number, input by user.
    b: Second number, input by user, default to 98 if not provided.
"""


def add_integer(a, b=98):
    """add_integer
    Adds two numbers together.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
