#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ class Rectangle that defines a rectangle """
    __height = None
    __width = None
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, prmWidth=0, prmHeight=0):
        self.height = prmHeight
        self.width = prmWidth
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, prmValue):
        if not isinstance(prmValue, int):
            raise TypeError("height must be an integer")
        if prmValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = prmValue

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, prmValue):
        if not isinstance(prmValue, int):
            raise TypeError("width must be an integer")
        if prmValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = prmValue

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        result = ""

        if self.height == 0 or self.width == 0:
            result += ''
        else:
            for row in range(self.height):
                result += str(self.print_symbol) * self.width
                if (row < self.height - 1):
                    result += '\n'
        return result

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(prmRectangleA, prmRectangleB):
        if not isinstance(prmRectangleA, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(prmRectangleB, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (prmRectangleA.area() is prmRectangleB.area() or
                prmRectangleA.area() > prmRectangleB.area()):
            return prmRectangleA
        else:
            return prmRectangleB
