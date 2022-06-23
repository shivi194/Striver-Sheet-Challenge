from os import *
from sys import *
from collections import *
from math import *

#    List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.pos = []

    def __del__(self):
        if (self.next):
            del self.next


def firstNode(head):
    if (head == None or head.next == None):
        return None
    slow = head
    fast = head
    slow = slow.next
    fast = fast.next.next
    while (fast and fast.next):
        if (slow == fast):
            break
        slow = slow.next
        fast = fast.next.next
    if (slow != fast):
        return None
    slow = head
    while (slow != fast):
        slow = slow.next
        fast = fast.next
    return slow