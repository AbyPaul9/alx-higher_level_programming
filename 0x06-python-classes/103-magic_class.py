#!/usr/bin/python3
""" Square class """

import math


class MagicClass:
    """ class MagicClass that defines a MagicClass
    Attributes:
        radisu: radius
    """
    __radius = None

    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        return self.__radius * math.pi * 2
