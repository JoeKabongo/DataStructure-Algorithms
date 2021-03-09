class EmptyStack(Exception):
    pass


class Stack:
    class Node:
        def __init__(self, data):
            self.val = data
            self.next = None

    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        if self.is_empty():
            raise EmptyStack("Empty stack cannot be popped")
            # return False

        item = self.top.val
        self.top = self.top.next
        self.size -= 1
        return item

    def push(self, item):
        new_item = self.Node(item)
        new_item.next = self.top
        self.top = new_item
        self.size += 1

    def peek(self):
        if self.is_empty():
            raise EmptyStack("Empty stack cannot be peeked")
        return self.top.val

    def is_empty(self):
        return self.top is None

    def __len__(self):
        return self.size
