#!/usr/bin/python3
def print_square(size):
    """
    Example:
        >>> try:
        ...     print_square(-9.8)
        ... except TypeError as e:
        ...     print(e)
        size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size)
