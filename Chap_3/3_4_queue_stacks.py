from stack import Stack
import unittest


class EmptyQueue(Exception):
    pass


class MyQueue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def add(self, value):
        self.enqueue_stack.push(value)

    def remove(self):
        if self.dequeue_stack.is_empty():
            if self.enqueue_stack.is_empty():
                raise EmptyQueue("Empty Qeueu cannot be dequeue")
            self.move_to_dequeue()

        return self.dequeue_stack.pop()

    def peek(self):
        if self.dequeue_stack.is_empty():
            if self.enqueue_stack.is_empty():
                raise EmptyQueue("Empty Qeueu cannot be peeked")
            self.move_to_dequeue()

        return self.dequeue_stack.peek()

    def move_to_dequeue(self):
        while self.enqueue_stack.is_empty():
            self.dequeue_stack.push(self.enqueue_stack.pop())

    def is_empty(self):
        return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()

    def __len__(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)
