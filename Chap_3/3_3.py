from stack import Stack
import unittest


class SetOfStacks:

    def __init__(self, capaticy):
        self.index = 0
        self.stacks = [Stack()]
        self.capaticy = capaticy

    def push(self, element):
        """ Push into the set of stack"""

        stack = self.stacks[self.index]

        # current stack equal max capacity
        if len(stack) == self.capaticy:
            self.stacks.append(Stack())
            self.index += 1
            stack = self.stacks[self.index]

        stack.push(element)

    def pop(self):
        """ Pop the latest element inserted"""
        if not self.is_empty():
            stack = self.stacks[self.index]
            element = stack.pop()
            if self.index > 0 and stack.is_empty():
                self.stacks.pop()
                self.index -= 1

            return element

    def pop_at(self, index):
        """ Pop element at stack index"""

        # make sure stack is valid
        if index < 0 or index > self.index:
            return

        stack = self.stacks[index]

        # make sure this stack is not empty
        if not stack.is_empty():
            element = stack.pop()
            if index != self.index:
                self.move_left(index + 1)
            return element

    def move_left(self, index):
        """ shift element to the left after pop_at """
        for i in range(index, self.index + 1):
            prev_stack = self.stacks[i-1]
            element = self.stacks[i].remove_bottom()
            prev_stack.push(element)

        # if the last stack is empty, remove it
        if len(self.stacks[self.index]) == 0:
            self.stacks.pop()
            self.index -= 1

    def is_empty(self):
        return self.index == 0 and self.stacks[0].is_empty()
