class EmptyQueue(Exception):
    pass


class Queue:
    class Node:
        def __init__(self, data):
            self.val = data
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        new_node = self.Node(item)
        if self.last is not None:
            self.last.next = new_node

        self.last = new_node
        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.isEmpty():
            raise EmptyQueue("Queue is Empty!")

        item = self.first.val
        self.first = self.first.next
        if self.first is None:
            self.last = None

        return item

    def peek(self):
        if self.isEmpty():
            raise EmptyQueue("Queue is Empty!")
        return self.first.val

    def isEmpty(self):
        return self.first is None
