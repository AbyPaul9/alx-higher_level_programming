#!/usr/bin/python3
""" lazy_matrix_mul module """


import numpy as np


def lazy_matrix_mul(prmMatrixA, prmMatrixB):
    """ lazy_matrix_mul function
    this function multiply one matrix by a second one
    Attributes:
        prmMatrixA: first matrix
        prmMatrixB: second matrix
    """
    if prmMatrixA is None:
        raise TypeError("m_a should be indicate")
    if prmMatrixB is None:
        raise TypeError("m_b should be indicate")
    if not isinstance(prmMatrixA, list):
        raise TypeError("m_a must be a list")
    if not isinstance(prmMatrixB, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(ele, list) for ele in prmMatrixA):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ele, list) for ele in prmMatrixB):
        raise TypeError("m_b must be a list of lists")
    if len(prmMatrixA) == 0 or len(prmMatrixA[0]) == 0:
        raise TypeError("m_a can't be empty")
    if len(prmMatrixB) == 0 or len(prmMatrixB[0]) == 0:
        raise TypeError("m_b can't be empty")

    arr1 = np.array(prmMatrixA)
    arr2 = np.array(prmMatrixB)
    return np.matmul(arr1, arr2)
