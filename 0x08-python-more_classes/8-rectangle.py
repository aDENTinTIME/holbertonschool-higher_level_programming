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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        errorChecks(width, "width")
        errorChecks(height, "height")
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        for x in range(self.height):
            print("{}".format(self.print_symbol) * self.width, end="")
            if x < self.height - 1:
                print()
        return ""

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
