from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    counter = 0
    probe = node
    while probe is not None:
        if index == counter:
            return probe
        counter += 1
        probe = probe.next
    raise IndexError

  