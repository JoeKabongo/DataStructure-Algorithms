# Algorithm to find kth element of a singly linkedlist
def kthToLast(head, k):
    if k < 1:
        return None

    slow_node = head
    fast_node = head

    index = 0
    while index < k and fast_node:
        fast_node = fast_node.next
        index += 1

    if index < k:
        return None

    while fast_node:
        slow_node = slow_node.next
        fast_node = fast_node.next

    return slow_node
