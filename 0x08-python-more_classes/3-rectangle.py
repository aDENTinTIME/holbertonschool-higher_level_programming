#!/usr/bin/python3
"""Defines an empty class, Rectangle
"""


def errorChecks(value, name):
    if not isinstance(value, int):
        raise TypeError(name + " must be an integer")
    if value < 0:
        raise ValueError(name + " must be >= 0")


class Rectangle:
    """Class Rectangle
    """
    def __init__(self, width=0, height=0):
        errorChecks(width, "width")
        errorChecks(height, "height")
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        for x in range(self.height):
            print("#" * self.width, end="")
            if x < self.height - 1:
                print()
        return ""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        errorChecks(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        errorChecks(value, "height")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
