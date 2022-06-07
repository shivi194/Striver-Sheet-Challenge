from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    row_index = set()
    col_index = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_index.add(i)
                col_index.add(j)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if col in col_index or row in row_index:
                matrix[row][col] = 0
    return matrix
	