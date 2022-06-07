from os import *
from sys import *
from collections import *
from math import *

def findTargetInMatrix(mat, m, n, target):
	# Write your code here.
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==target:
                return True
    return False        
	