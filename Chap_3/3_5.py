from stack import Stack


def sort_stack(s1):
    """Sort Stack s1 using an additional Stack """
    s2 = Stack()
    while not s1.is_empty():
        s2.push(s1.pop())

    while not s2.is_empty():
        element = s2.pop()
        while not s1.is_empty() and s1.peek() < element:
            s2.push(s1.pop())

        s1.push(element)


x = Stack()
x.push(10)
x.push(4)
x.push(11)
x.push(34)
x.push(1)

sort_stack(x)
while not x.is_empty():
    print(x.pop())
