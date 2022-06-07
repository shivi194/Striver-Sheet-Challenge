from os import *
from sys import *
from collections import *
from math import *

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    res=[]

    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j==i or j==0:
                temp_list.append(1)
            else:
                s = res[i-1][j-1] + res[i-1][j]
                temp_list.append(s)
        res.append(temp_list) 
    return res