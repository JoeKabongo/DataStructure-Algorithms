from stack import Stack


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_values = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.min_values.is_empty() or item <= self.min_values.peek():
            self.min_values.push(item)

    def pop(self):
        element = self.stack.pop()
        if element == self.min_values.peek():
            self.min_values.pop()
        return element

    def get_min(self):
        return self.min_values.peek()
