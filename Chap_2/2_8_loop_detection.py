from node import Node


def linkedlist_beginning(head) -> ListNode:
    """Find start of loop in linkedlist """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            break

    # there is no loop in the linkedlist
    if fast is None or fast.next is None:
        return None

    slow = head

    # both slow and fast will be k step away from the start of loops
    while slow != fast:
        fast = fast.next
        slow = slow.next

    return fast
