#!/usr/bin/python3


class MyInt(int):
    """Not working at the moment
    """
    def __eq__(self, other):
        return (self is other)

    def __ne__(self, other):
        return (self is not other)
