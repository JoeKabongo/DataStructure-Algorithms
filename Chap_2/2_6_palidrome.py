def is_palidrome(head):
    """ Return either head is a palidrom or not"""
    if head is None or head.next is None:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # for odd lenght of linkedlist
    if fast:
        slow = slow.next

    # reverse the second half of the linkedlist
    right_reverse = reverse(slow)
    left = head

    while right_reverse:
        # not a palifrom
        if right_reverse.val != left.val:
            return False
        right_reverse = right_reverse.next
        left = left.next

    return True


def reverse(node):
    prev = None
    while node:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node

    return prev


def is_palindrome2(head: ListNode) -> bool:
    """This time using a stack"""
    if head is None or head.next is None:
        return True

    slow = head
    fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while stack:
        if stack.pop() != slow.val:
            return False
        slow = slow.next

    return True
