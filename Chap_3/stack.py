class EmptyStack(Exception):
    """ A wrapper exception to hide implementation details """
    pass


class Stack:
    class Node:
        def __init__(self, data):
            self.val = data
            self.next = None

    def __init__(self):
        self.top = None

    def pop(self):
        if self.isEmpty():
            raise EmptyStack("Empty stack cannot be popped")

        item = self.top.val
        self.top = self.top.next
        return item

    def push(self, item):
        new_item = self.Node(item)
        new_item.next = self.top
        self.top = new_item

    def peek(self):
        if self.isEmpty():
            raise EmptyStack("Empty stack cannot be peeked")
        return self.top.val

    def isEmpty(self):
        return self.top is None
