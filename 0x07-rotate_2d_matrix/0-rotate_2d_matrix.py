#!/usr/bin/python3
''' 2D matrix rotation clockwise '''


def rotate_2d_matrix(matrix):
    '''
        rotates 2d matrix 90 degrees clockwise
        args:
            matrix
    '''
    rows = len(matrix)
    columns = rows - 1

    for i in range(0, int(rows / 2)):
        for j in range(i, columns - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[columns - j][i]
            matrix[columns - j][i] = matrix[columns - i][columns - j]
            matrix[columns - i][columns - j] = matrix[j][columns - i]
            matrix[j][columns - i] = temp