from os import *
from sys import *
from collections import *
from math import *

# List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.child = None

    def __del__(self):
        if(self.next):
            del self.next


def flattenLinkedList(head):
    if head == None or head.next == None:
        return head
    head.next = flattenLinkedList(head.next)
    head = merge(head,head.next)
    return head

def merge(h1,h2):
    if h1 == None:
        return h2
    if h2 == None:
        return h1
    result = None
    if h1.data<h2.data:
        result = h1
        result.child = merge(h1.child,h2)
    else:
        result = h2
        result.child = merge(h1,h2.child)
    result.next = None
    return result
        
               