from BST import TreeNode


def is_balanced(node: TreeNode) -> bool:
    if node is None:
        return True

    return check_balanced(node) != -1


def check_balanced(node: TreeNode):
    if node is None:
        return 0

    left = check_balanced(node.left)
    right = check_balanced(node.right)

    if left == -1 or right == -1:
        return -1

    if abs(left-right) > 1:
        return - 1

    return 1 + max(right, left)
