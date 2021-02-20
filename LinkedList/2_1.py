from . import Node


# removing duplicate from an unsorted LinkedList
def removeDuplicate(head):
    if head is None:
        return

    set_values = set()
    set_values.add(head.val)
    node = head

    while node.next:
        if node.next.val in set_values:
            node.next = node.next.next
        else:
            set_values.add(node.next.val)
            node = node.next


# remove duplicate without using space
def removeDuplicateNospace(head):
    if head is None:
        return head

    node = head
    while node.next:
        cursor = node
        while cursor.next:
            if cursor.next.val == node.val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next

        node = node.next
