#!/usr/bin/python3
"""
Function(s):
    say_my_name: Says the given name.
"""


def say_my_name(first_name, last_name=""):
    """
    Recieves two values, checks if they're both strings, raises a TypeError
    if not. They are both then printed, prefaced with `My name is`.

    Args:
        first_name: First name provided.
        last_name: Last name provided, default to empty string.

    Raises:
        TypeError: In the event of either variable not being a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
