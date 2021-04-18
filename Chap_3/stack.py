class EmptyStack(Exception):
    pass


class Stack:
    class Node:
        def __init__(self, data):
            self.val = data
            self.previous = None
            self.next = None

    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def pop(self):
        """ Pop top of the stack"""
        if self.is_empty():
            raise EmptyStack("Empty stack cannot be popped")
            # return False

        item = self.top.val
        self.top = self.top.next
        if self.top:
            self.top.previous = None
        else:
            self.bottom = None

        self.size -= 1
        return item

    def remove_bottom(self):
        """ Remove element on the bottom of stack"""
        if self.is_empty():
            raise EmptyStack("Empty stack cannot be popped")
        element = self.bottom.val
        self.bottom = self.bottom.previous

        if self.bottom is None:
            self.top = None
        else:
            self.bottom.next = None

        self.size -= 1

        return element

    def push(self, item):
        """ Push element on top of the stack"""
        new_item = self.Node(item)
        new_item.next = self.top
        if self.top:
            self.top.previous = new_item

        self.top = new_item
        self.size += 1

        if self.bottom is None:
            self.bottom = self.top

    def peek(self):
        if self.is_empty():
            raise EmptyStack("Empty stack cannot be peeked")
        return self.top.val

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        result = "["
        node = self.top
        while node:
            result += str(node.val) + ", "
            node = node.next
        result += "]"
        return result
