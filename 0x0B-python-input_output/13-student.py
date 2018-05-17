#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            dic = {}
            for x in attrs:
                if self.__dict__.__contains__(x):
                    dic[x] = self.__dict__[x]
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        pass
