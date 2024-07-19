#!/usr/bin/python3
"""function returns True if object is exactly
an instance of the specified class
Else, returns False"""


def is_same_class(obj, a_class):
    """Method declaration"""
    return type(obj) is a_class
