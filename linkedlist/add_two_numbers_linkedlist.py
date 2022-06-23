from os import *
from sys import *
from collections import *
from math import *

# List Node Class.
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next


def addTwoNumbers(head1, head2):
    temp = Node(0)
    ptr1 = head1
    ptr2 = head2
    curr = temp; carry = 0
    while ptr1 or ptr2:
        x = ptr1.data if ptr1 else 0
        y = ptr2.data if ptr2 else 0
        s = x+y+carry
        carry = s//10
        curr.next = Node(s%10)
        curr = curr.next
        if ptr1:
            ptr1 = ptr1.next
        if ptr2:
            ptr2 = ptr2.next
    if carry:
        curr.next = Node(carry)
        
    return temp.next