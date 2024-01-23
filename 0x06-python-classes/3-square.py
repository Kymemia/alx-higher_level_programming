#!/usr/bin/python3

"""class, Square, that defines a square"""


class Square:
    """square definition"""
    def __init__(self, size=0):
        """definition of private instance attribute"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """public instance method to return the current square area"""
        return self.__size ** 2
