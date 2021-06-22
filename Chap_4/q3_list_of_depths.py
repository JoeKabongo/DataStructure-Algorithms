from BST import TreeNode
from q2_minimal_tree import minimal_tree
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.root
        self.root = new_node

    def __str__(self):
        node = self.root
        result = ""
        while node:
            result += str(node.value) + "-> "
            node = node.next

        result += "None"
        return result


def list_of_depth(node: TreeNode) -> [Node]:
    output = []
    create_level(node, 0, output)
    return output


def list_of_depth_iterative(node: TreeNode) -> [Node]:
    output = []
    if node is None:
        return output

    else:
        level = deque()
        level.append(node)

        while len(level):
            size = len(level)
            level_linkedlist = LinkedList()
            for i in range(size):
                node = level.popleft()
                level_linkedlist.insert(node.key)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            output.append(level_linkedlist)
    return output


def create_level(node: TreeNode, index, output):
    if node is None:
        return

    if index == len(output):  # level is not in the list yet
        output.append(LinkedList())

    output[index].insert(node.key)

    create_level(node.left, index + 1, output)
    create_level(node.right, index + 1, output)


x = minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
array = list_of_depth(x)
array1 = list_of_depth_iterative(x)
for l in array:
    print(l)

print("  ")
for l in array1:
    print(l)
