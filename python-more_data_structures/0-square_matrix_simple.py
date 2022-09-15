#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for INT in range(len(matrix)):
        new_matrix[INT] = list(map(lambda x: x**2, matrix[INT]))
    return (new_matrix)
