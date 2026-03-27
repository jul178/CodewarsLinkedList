def loop_size(node):
    fast = node
    slow = node

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            lenght = 1
            fast = fast.next

            while fast != slow:
                fast = fast.next
                lenght += 1
            return lenght
