#!/usr/bin/python3
"""class, Rectangle, that defines a rectangle"""


class Rectangle:
    """Class definition"""
    def __init__(self, width=0, height=0):
        """width + height definition"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance method
        that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """public instance method
        that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
