#!/usr/bin/python3
""" Square class """


class Square:
    """ empty class Square that defines a square
    Attributes:
        size: size of the square
        position: square margins
    """
    __size = 0
    __position = 0

    def __init__(self, prmSize=0, prmPosition=(0, 0)):
        self.size = prmSize
        self.position = prmPosition

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, prmSize=0):
        if not isinstance(prmSize, int):
            raise TypeError("size must be an integer")
        elif prmSize < 0:
            raise ValueError("size must be >= 0")
        self.__size = prmSize

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for row in range(self.position[1]):
                print()
            for column in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, prmPosition):
        if (not isinstance(prmPosition, tuple) or
                list(map(type, prmPosition)) != [int, int] or
                sum(0 if i >= 0 else 1 for i in prmPosition)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = prmPosition
