from os import *
from sys import *
from collections import *
from math import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    prev = None
    curr=head
    next = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev    
    
