

class Node:
    def __init__(self, aValue):
        self.val = aValue
        self.next = None


def add(node1, node2):
    return add_helper(node1, node2, 0)


def add_helper(node1, node2, carry):
    if node1 is None and node2 is None and carry == 0:
        return None

    new_node = Node(0)

    val = carry
    if node1:
        val += node1.val
        node1 = node1.next

    if node2:
        val += node2.val
        node2 = node2.next

    new_node.val = val % 10
    carry = 0 if val < 10 else 1
    new_node.next = add_helper(node1, node2, carry)
    return new_node


def add_interative(head1, head2):
    dummy = Node(0)
    current = dummy
    carry = 0

    while head1 or head2 or carry:
        val = carry
        if head1:
            val += head1.val
            head1 = head1.next

        if head2:
            val += head2.val
            head2 = head2.next

        current.next = Node(val % 10)
        carry = 0 if val < 10 else 1
        current = current.next

    return dummy.next


def display(node):
    while node:
        print(f"{node.val} -> ", end="")
        node = node.next

    print(" None")


def constructNode(array):
    head = Node(0)
    current = head

    for element in array:
        current.next = Node(element)
        current = current.next

    return head.next


head1 = constructNode([9, 7, 8])
head2 = constructNode([6, 8, 5])
display(add_interative(head1, head2))
