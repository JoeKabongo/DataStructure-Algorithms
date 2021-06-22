from BST import TreeNode
from q2_minimal_tree import minimal_tree


def is_valid(node: TreeNode):
    return check_valid(node, float('-inf'), float('inf'))


def check_valid(node, min_limit, max_limit):
    if node is None:
        return True

    if node.key < min_limit or node.key > max_limit:
        return False

    return check_valid(node.left, min_limit,  node.key) and check_valid(node.right, node.key, max_limit)


x = minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print(is_valid(x))
