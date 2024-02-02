#!/usr/bin/python3
"""adds 2 integers"""


def add_integer(a, b=98):
    """returns the sum of int a and int b"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

def int_conversion(num):
    """convert a float to int"""
    if type(num) is float:
        num = int(num)
        return num
    return num
