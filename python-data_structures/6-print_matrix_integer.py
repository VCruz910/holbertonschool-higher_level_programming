#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for X in range(len(matrix)):
        for Y in range(len(matrix[X])):
            if Y != 0:
                print(" ", end='')
            print("{:d}".format(matrix[X][Y]), end='')
        print()
