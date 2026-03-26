class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    reversed_head = None
    probe = head
    while probe is not None:
        nextNode = probe.next
        probe.next = reversed_head
        reversed_head = probe
        probe = nextNode

    return reversed_head
    