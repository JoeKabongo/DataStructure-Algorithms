def intersection_node(headA, headB):
    """
        Return node on which the two linklist intersect, if they do
    """
    l1 = get_length(headA)
    l2 = get_length(headB)

    diff = abs(l1 - l2)
    if l1 < l2:
        for i in range(diff):
            headB = headB.next
    else:
        for i in range(diff):
            headA = headA.next

    while headA:
        if headA == headB:
            return headA

        headA = headA.next
        headB = headB.next

    return None


def get_length(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count
