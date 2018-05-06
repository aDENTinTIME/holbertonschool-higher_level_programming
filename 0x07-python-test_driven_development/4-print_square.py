#!/usr/bin/python3
"""
Function(s):
    print_square: Prints a square.
"""


def print_square(size):
    """
    Recieves one value, varifies it's an int, and greater than zero,
    appropriate errors are raised if not. Then prints a square of `#`
    of corresponding size.

    Args:
        size: User specified size of square.

    Raises:
        TypeError: In the event of the variable not being an int.
        ValueError: In the event of the int being less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size)
