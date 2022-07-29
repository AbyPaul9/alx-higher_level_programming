#!/usr/bin/python3
""" matrix_divided module """


def matrix_divided(prmMatrix, prmDiv):
    """ matrix_divided function
    Attributes:
        prmMatrix: matrix of value
        prmDiv: number to divide each value of the matrix
    """
    errTypeMsg = "matrix must be a matrix (list of lists) of integers/floats"
    errSameSizeMsg = "Each row of the matrix must have the same size"
    if not all(isinstance(ele, list) for ele in prmMatrix):
        raise TypeError(errTypeMsg)

    new = prmMatrix.copy()
    rowLen = len(new)

    if rowLen > 0:
        columnLen = len(new[0])

        for row in range(len(new)):
            if not all(isinstance(ele, (int, float)) for ele in new[row]):
                raise TypeError(errTypeMsg)
            if len(new[row]) != columnLen:
                raise TypeError(errSameSizeMsg)

        if not isinstance(prmDiv, int):
            raise TypeError("div must be a number")
        if prmDiv == 0:
            raise ZeroDivisionError("division by zero")

        for row in range(len(new)):
            for column in range(len(new[row])):
                new[row][column] = round(float(new[row][column] / prmDiv), 2)
		return new
