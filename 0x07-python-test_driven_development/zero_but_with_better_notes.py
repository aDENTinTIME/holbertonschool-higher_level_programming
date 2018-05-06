#!/usr/bin/python3
"""
Contains:
    add_integer
"""


def add_integer(a, b=98):
    """
    Recieves two values, checks if they're numbers, casts them as ints
    and returns the result of their addition. If either value is not
    a number, a TypeError is raised.

    Args:
        a: First number, input by user.
        b: Second number, input by user, default to 98 if not provided.

    Returns:
        int: Result of addition of a and b.

    Raises:
        TypeError: in the event of either variable
            not being an int or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
