class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def successor(node: TreeNode):
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor
    else:
        parent_node = node
        while parent_node and parent_node.left != node:
            node = parent_node
            parent_node = parent_node.parent
        return parent_node
