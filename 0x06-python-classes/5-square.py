#!/usr/bin/python3

"""class, Square, that defines a square"""


class Square:
    """class definition"""
    def __init__(self, size=0):
        """size definition"""
        self.size = size

    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """public instance that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """public instance that prints
        in stdout the square with the character, #"""
        for _ in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            pass
