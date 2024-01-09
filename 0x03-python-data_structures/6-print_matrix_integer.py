#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    colums = 3
    for row in matrix:
        new_row = ''
        for element in row:
            new_row += f'{element:<4d}'
        print(new_row[:-1])
