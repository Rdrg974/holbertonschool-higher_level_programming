#!/usr/bin/python3


def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    matrix_cpy = [row[:] for row in matrix]
    for i in range(len(matrix_cpy)):
        for j in range(len(matrix_cpy[i])):
            matrix_cpy[i][j] = round(float(matrix_cpy[i][j]) / div, 2)
    return matrix_cpy
