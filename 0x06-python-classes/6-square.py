#!/usr/bin/python3

"""class, Square, that defines a square"""


class Square:
    """Class definition"""
    def __init__(self, size=0, position=(0, 0)):
        """size + position definition"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """property to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter to set it"""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """public instance method that prints
        in stdout the square with the character, #"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
