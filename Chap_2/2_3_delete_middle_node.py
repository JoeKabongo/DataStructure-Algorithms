def delete_node(node):
    """ delete a node in a linkedlist, given reference to that only"""
    if node is None or node.next is None:
        return

    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next
