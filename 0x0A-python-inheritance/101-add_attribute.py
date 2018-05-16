#!/usr/bin/python3


def add_attribute(instance, attribute, value):

    if isinstance(attribute, type(instance)):
        raise TypeError("can't add new attribute")
    else:
        setattr(instance, attribute, value)
