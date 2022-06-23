from os import *
from sys import *
from collections import *
from math import *

import sys
from sys import stdin

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(first, second):
    if not first and not second:
        return None
    if not first:
        return second
    if not second:
        return first
    if first.data<second.data:
        first.next = sortTwoLists(first.next,second)
        return first
    else:
        second.next = sortTwoLists(first,second.next)
        return second
    










def ll(arr):
    
    if len(arr)==0:
        return None
    
    head = Node(arr[0])
    last = head
    
    for data in arr[1:]:
        
        last.next = Node(data)
        last = last.next
        
    return head

def printll(head):
    
    while head:
        
        print(head.data, end=' ')
        
        head = head.next
        
    print(-1)

    

t = int(sys.stdin.readline().strip())

for i in range(t):
    
    arr1=list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2=list(map(int, sys.stdin.readline().strip().split(" ")))
    
    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])
    
    l = sortTwoLists(l1, l2)
    
    printll(l)

