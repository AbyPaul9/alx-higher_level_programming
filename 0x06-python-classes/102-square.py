#!/usr/bin/python3
""" Square class """


class Square:
    """ empty class Square that defines a square
    Attributes:
        size: size of the square
    """
    __size = 0

    def __init__(self, prmSize=0):
        self.size = prmSize

    def __eq__(self, prmObject):
        if not isinstance(prmObject, Square):
            raise TypeError("object should be square type object")
        return self.size == prmObject.size

    def __ne__(self, prmObject):
        if not isinstance(prmObject, Square):
            raise TypeError("object should be square type object")
        return not self.__eq__(prmObject)

    def __gt__(self, prmObject):
        if not isinstance(prmObject, Square):
            raise TypeError("object should be square type object")
        return self.size > prmObject.size

    def __lt__(self, prmObject):
        if not isinstance(prmObject, Square):
            raise TypeError("object should be square type object")
        return self.size < prmObject.size

    def __ge__(self, prmObject):
        if not isinstance(prmObject, Square):
            raise TypeError("object should be square type object")
        return self.size >= prmObject.size

    def __le__(self, prmObject):
        if not isinstance(prmObject, Square):
            raise TypeError("object should be square type object")
        return self.size <= prmObject.size

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
