#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_idx = 0
    while row_idx < len(matrix):
        col_idx = 0
        while col_idx < len(matrix[row_idx]):
            col = matrix[row_idx][col_idx]
            print('{:d}'.format(col),
                    end=' ' if col_idx < len(matrix[row_idx]) - 1 else '')
            col_idx += 1
        print()
        row_idx += 1
