#!/usr/bin/python3

"""class, Rectangle, that defines a rectangle"""


class Rectangle:
    """class definition"""
    def __init__(self, width=0, height=0):
        """width+size defintion"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

    @property
    def height(self):
        """property to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """public instance method that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints message"""
        if self.__width == 0 or self.__height == 0:
            return ""
        fig = []
        for x in range(self.__height):
            [fig.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                fig.append('\n')
        return ''.join(fig)

    def __repr__(self):
        """return string representation"""
        fig = "Rectangle(" + str(self.__width)
        fig += ", " + str(self.__height) + ")"
        return fig
