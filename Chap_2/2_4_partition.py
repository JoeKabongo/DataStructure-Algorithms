from . import Node


def partition(head, value):
    if head is None or head.next is None:
        return head

    prev = head
    node = head.next
    while node:
        if node.val < value:
            prev.next = node.next
            node.next = head
            head = node
            node = prev.next
        else:
            prev = node
            node = node.next

    return head


# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
def partition_stable(head, value):
    left = left_head = Node(0)
    right = right_head = Node(0)

    node = head
    while node:
        if node.val < value:
            left.next = node
            left = node
        else:
            right.next = node
            right = node
        node = node.next

    right.next = None
    left.next = right_head.next
    return right_head.next
