#!/usr/bin/python3

"""class, Square, that defines a square"""


class Square:
    """class definition"""
    def __init__(self, size=0):
        """self + size definition"""
        self.size = size

    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it"""
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """public instance method
        that returns the current square area"""
        return self.__size ** 2

    def __gt__(self, other):
        """greater than"""
        return self.area() > other.area()

    def __le__(self, other):
        """less than or equal to"""
        return self.area() <= other.area()

    def __ge__(self, other):
        """greater than or equal to"""
        return self.area() >= other.area()

    def __eq__(self, other):
        """equal"""
        return self.area() == other.area()

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __ne__(self, other):
        """not equal to"""
        return self.area() != other.area()
