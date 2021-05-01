class EmptyStack(Exception):
    pass


class StackInfo:
    def __init__(self, start_index, next_index, end_index):
        """Keep track of stack indexes in the arra"""
        self.start_index = start_index
        self.next_index = next_index
        self.last_index = end_index

    def increment(self):
        self.next_index += 1

    def decrement(self):
        self.next_index -= 1

    def is_full(self):
        return self.next_index > self.last_index

    def is_empty(self):
        return self.next_index == self.start_index

    def size(self):
        return self.last_index - self.start_index + 1

    def get_start(self):
        return self.start_index

    def get_next(self):
        return self.next_index

    def get_start_next_difference(self):
        return self.next_index - self.start_index

    def get_end(self):
        return self.last_index

    def set_start(self, value):
        self.start_index = value

    def set_next(self, value):
        self.next_index = value

    def set_end(self, value):
        self.last_index = value

    def set_values(self, start_index, next_index, last_index):
        self.start_index = start_index
        self.next_index = next_index
        self.last_index = last_index

    def __str__(self):
        return f"Start index={self.start_index}, Next index={self.next_index}, last Index{self.last_index}"


class TheeStacks:
    def __init__(self):
        """ 
            Three stack using one array
            Start of with an array of 9, each stack has capacity three
        """
        self.array = [None] * 9
        self.array_size = 9
        self.stacks_info = [StackInfo(0, 0, 2), StackInfo(
            3, 3, 5), StackInfo(6, 6, 8)]

    def pop(self, stack_num):
        """ Pop operation for a particular stack"""
        if 1 <= stack_num <= 3:
            stack = self.stacks_info[stack_num-1]
            if stack.is_empty():
                raise EmptyStack("Empty stack cannot be popped")

            index = stack.get_next() - 1
            item = self.array[index]
            self.array[index] = None
            stack.decrement()
            return item

        else:
            raise ValueError("stack number must be between 1 and 3")

    def peek(self, stack_num):
        """ Peek for a particular stack"""
        if 1 <= stack_num <= 3:
            stack = self.stacks_info[stack_num-1]
            if stack.is_empty():
                raise EmptyStack("Empty stack cannot be peeked")

            index = stack.get_next() - 1
            item = self.array[index]
            return item

        else:
            raise ValueError("stack number must be between 1 and 3")

    def push(self, stack_num, element):
        """ Push operation for a particula stack"""
        if 1 <= stack_num <= 3:
            stack = self.stacks_info[stack_num-1]
            if stack.is_full():
                self.expand_stack(stack_num-1)

            next_index = stack.get_next()
            self.array[next_index] = element
            stack.increment()

        else:
            raise ValueError("stack number must be between 1 and 3")

    def expand_stack(self, stack_index):
        """ expand the size of stack at stack_index"""
        # new_array current size + stack_info[index] size
        # pretty much double the size of the size considered
        new_array = [None] * (self.array_size +
                              self.stacks_info[stack_index].size())

        # compute infos of new_stacks info value
        index = 0
        new_stacks_info = []
        for i in range(3):
            new_stack = self.compute_new_stack(index, i, stack_index)
            index += new_stack.size()
            new_stacks_info.append(new_stack)

        # copy old value into new_array
        for i in range(3):
            old_stack = self.stacks_info[i]
            old_size = old_stack.size()
            old_index = old_stack.get_start()
            start = new_stacks_info[i].get_start()
            for j in range(start, start + old_size):
                new_array[j] = self.array[old_index]
                old_index += 1

        # update to new array and new_stack infos
        self.array = new_array[:]
        self.stacks_info = new_stacks_info
        self.array_size = len(self.array)

    def compute_new_stack(self, index, current_stack, expanded_index):
        """ Compute the new indexes info of the new_stack
            index: new_start of current_stack
            current_stack: index of the stack considered
            extended_stack: stack to be expanded
        """
        old_stack = self.stacks_info[current_stack]
        size = old_stack.size()

        # double the size if it is the stack that needs to be expanded
        if current_stack == expanded_index:
            size *= 2

        # compute where the next value will go in new_stack
        new_next = index + (old_stack.get_start_next_difference())
        return StackInfo(index, new_next, index + size - 1)

    def print_stack(self, stack_index):
        stack = self.stacks_info[stack_index]
        start = stack.get_start()
        end = stack.get_end()
        print(self.array[start: end+1])


s = TheeStacks()

s.push(1, 10)
s.push(1, 39)
s.push(1, 32)
s.push(1, 9)

s.push(2, 89)
s.push(2, 21)
s.push(2, 32)
s.push(2, 66)

s.push(3, 4)
s.push(3, 100)
s.push(3, 22)
s.push(3, 121)

for i in range(0, 3):
    s.print_stack(i)
