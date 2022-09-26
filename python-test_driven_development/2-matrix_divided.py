#!/usr/bin/python3
"""
Module: Matrix Divided
Divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides the integer/
    floats of a matrix.

    Args:
        matrix: A list of lists of
        integers/floats
    Returns:
        Returns a new matrix with the
        results of the division of the
        matrix by dividing it rounded
        to two decimals.
    Raises:
        TypeError:
            If the elements of the aren't list,
            integers/floats.

            If the div of the matrix is not
            integers/floats.

            If the lists of the matrix are not
            the same size.
    Zero Division Error:
            If div is zero.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)" +
        " of integers/floats")

    for ROW in matrix:
        if len(ROW) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
            " of integers/floats")
        for X in ROW:
            if type(X) is not int and type(X) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                " of integers/floats")

    LEN_RW = []

    for ROW in matrix:
        LEN_RW.append(len(ROW))

    if not all(ELE == LEN_RW[0] for ELE in LEN_RW):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    NewMatrix = [[round(X / div, 2) for X in ROW] for ROW in matrix]

    return (NewMatrix)
