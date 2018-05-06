#!/usr/bin/python3
"""
Function(s):
    text_indentation: Breaks up a string by `.?:`.
"""


def text_indentation(text):
    """
    Recieves one value, checks if it's a string, raising a TypeError if not.
    The text is then parsed and split up by the delimiters `.?:`.
    Two new lines are put after each occurence of the delimter.
    Any trailing spaces on either side of each line will be removed.

    Args:
        text: String input by user.

    Raises:
        TypeError: In the event the variable is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = text.split(".")
    new = [x.strip(" ") for x in new]
    new = '.\n\n'.join(new)

    new = new.split("?")
    new = [x.strip(" ") for x in new]
    new = '?\n\n'.join(new)

    new = new.split(":")
    new = [x.strip(" ") for x in new]
    new = ':\n\n'.join(new)

    print(new, end="")
