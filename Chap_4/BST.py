class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, key, value):
        """ Insert key and value iteratavely """
        if self.root is None:
            self.root = Node(key, value)

        prev = None
        node = self.root

        while node:
            prev = node
            if node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left
            else:  # key was already in the BST, just update the value
                node.value = value
                return

        if prev.key < key:
            prev.right = Node(key, value)
        else:
            prev.left = Node(key, value)

    def insert_recursive(self, key, value):
        """ insert new key and value recusrively """
        self.root = self.recursive_helper(self.root, key, value)

    def recursive_helper(self, node, key, value):
        if node is None:
            return Node(key, value)

        if node.key < key:
            node.right = self.recursive_helper(node.right, key, value)

        elif node.key > key:
            node.left = self.recursive_helper(node.left, key, value)

        else:  # key was already in the BST, just update the value
            node.value = value

        return node

    def contains(self, key):
        pass

    def get(self, key):
        pass

    def inorder(self):
        def helper(node):
            if node:
                helper(node.left)
                print(node.key)
                helper(node.right)

        helper(self.root)
