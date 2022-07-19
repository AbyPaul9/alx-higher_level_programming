#!/usr/bin/python3
""" Square class """


class Square:
    """ empty class Square that defines a square
    Attributes:
        size: size of the square
    """
    __size = 0

    def __init__(self, prmSize=0):
        if not isinstance(prmSize, int):
            raise TypeError("size must be an integer")
        if prmSize < 0:
            raise ValueError("size must be >= 0")
        self.__size = prmSize

    def area(self):
        return self.__size ** 2
