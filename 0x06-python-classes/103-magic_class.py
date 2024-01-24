import math

"""class, MagicClass, that does exactly the same as a bytecode"""


class MagicClass:
    def __init___(self, r=0):
        self.__radius = 0

        if type(r) is not float or type(r) is not int:
            raise TypeError('r must be a number')

        self.__r = r

    def area(self):
        """returns area of a circle"""
        return math.pi * self.__r ** 2

    def circumference(self):
        """returns the circumference"""
        return math.pi * self.__r * 2
