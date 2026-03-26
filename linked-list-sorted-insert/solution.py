class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

        
def sorted_insert(head, data):
    if head is None:
        head = Node(data)
        return head

    if data <= head.data:
        node = Node(data)
        node.next = head
        return node

    probe = head
    while probe.next is not None and probe.next.data < data:
        probe = probe.next

    node = Node(data)
    node.next = probe.next
    probe.next = node

    return head
