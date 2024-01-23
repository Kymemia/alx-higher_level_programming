#!/usr/bin/python3

"""Class, Square, that defines a square"""


class Square:
    """class definition"""
    def __init__(self, size=0):
        """size definition"""
        self.size = size

    @property
    def size(self):
        """retrieve size with getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter property"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """public instance method to return the current square area"""
        return self.__size ** 2
