#!/usr/bin/python3
"""Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
       Rotates 2D matrix 90 degrees clockwise
       Matrix is edited in-place
       args:
          matrix
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
