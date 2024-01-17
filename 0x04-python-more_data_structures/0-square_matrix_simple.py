#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        for w in range(len(matrix[i])):
            matrix[i][w] = matrix[i][w] ** 2
    return matrix
