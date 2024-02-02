#!/usr/bin/python3
"""Module that adds 2 numbers

This is a module that adds two numbers.
First, it casts integers if they are float.
"""


def add_integer(a, b=98):
    """returns the sum of int a and int b

    Args:
        a (:obj: 'int, float'): The first number
        b (:obj: int, float', optional): The second number

    Returns:
        int: sum as an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

def int_conversion(num):
    """convert a float to int

    Args:
        num(:obj: 'int, float'): Number to cast

    Returns:
        int: number to be cast
    """
    if type(num) is float:
        num = int(num)
        return num
    return num
