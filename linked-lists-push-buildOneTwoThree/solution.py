from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    lst = None
    lst = push(lst, 3)
    lst = push(lst, 2)
    lst = push(lst, 1)
    return lst
