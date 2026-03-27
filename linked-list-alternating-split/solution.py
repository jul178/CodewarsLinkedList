class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    first = head
    second = head.next

    f = first
    s = second

    probe = head.next.next
    toggle = True
    while probe is not None:
        if toggle:
            f.next = probe
            f = f.next
        else:
            s.next = probe
            s = s.next
        probe = probe.next
        toggle = not toggle

    f.next = None
    s.next = None

    return Context(first, second) 
