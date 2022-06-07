from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
            
def isPalindrome(head):
    store = []
    temp = head
    while temp:
        store.append(temp.data)
        temp = temp.next
    store = store[::-1]
    temp = head
    j = 0
    while temp:
        if temp.data!=store[j]:
            return False
        j=j+1
        temp = temp.next
    return True    
    
    
    
def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        if currentData == -1:
            break
        
        Newnode=Node(currentData)
        
        if head is None:
            head=Newnode
            tail=Newnode
        else:
            tail.next=Newnode
            tail=Newnode
            
    return head


#Main
t = int(stdin.readline().rstrip())

while t > 0:
    
    head = takeinput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1
