from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None

    values = list_repr.split(' -> ')
    head = Node(int(values[0]))
    node = head
    for v in values[1:]:
        if v == 'None':
            break
        node.next = Node(int(v))
        node = node.next
    return head
