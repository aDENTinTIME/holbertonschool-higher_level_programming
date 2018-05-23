#!/usr/bin/python3
"""Base class
"""


import json


class Base:
    """
    class Base is the highest class, forming a fundamental layer
    of all it's sub-classes. It will keep a count of how many times
    an object of it's class has been instantiated OR not if an ID
    is provided.

    Args:
        id: The desired ID of an object's instance, or the next available ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
