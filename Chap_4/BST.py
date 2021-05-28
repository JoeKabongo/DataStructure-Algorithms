class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, key):
        """ Insert key iteratavely """
        if self.root is None:
            self.root = TreeNode(key)

        prev = None
        node = self.root

        while node:
            prev = node
            if node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left
            else:  # key was already in the BST, just update the value
                return

        if prev.key < key:
            prev.right = TreeNode(key)
        else:
            prev.left = TreeNode(key)

    def insert_recursive(self, key):
        """ insert new key """
        self.root = self.recursive_helper(self.root, key)

    def recursive_helper(self, node, key, value):
        if node is None:
            return TreeNode(key)

        if node.key < key:
            node.right = self.recursive_helper(node.right, key)

        elif node.key > key:
            node.left = self.recursive_helper(node.left, key)

        else:  # key was already in the BST, just update the value
            return node

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
