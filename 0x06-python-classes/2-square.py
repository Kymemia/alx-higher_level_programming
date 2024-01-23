#!/usr/bin/python3

"""this be a class that defines a square"""


class Square:
    """square definition"""
    def __init__(self, size=0):
        """definition of private instance attribute named, size"""
        if not isinstance(size, int):
            raise ValueError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
