from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    probe = head
    nextnode = head.next
    rest = nextnode.next

    nextnode.next = probe
    probe.next = rest
    head = nextnode

    prevNode = probe

    while prevNode.next is not None and prevNode.next.next is not None:
        probe = prevNode.next
        nextnode = prevNode.next.next
        rest = nextnode.next

        prevNode.next = nextnode
        nextnode.next = probe
        probe.next = rest

        prevNode = probe
    return head
