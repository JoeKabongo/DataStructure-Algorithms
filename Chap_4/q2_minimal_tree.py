from BST import TreeNode
from collections import deque


def minimal_tree(A):
    """
    given a sorted array A, create a cree with minimal height
    """
    N = len(A)
    if N == 0:
        return None
    return helper(A, 0, len(A) - 1)


def helper(A, start, end):
    if start > end:
        return None
    middle = (start + end)//2
    x = TreeNode(A[middle])
    x.left = helper(A, start, middle - 1)
    x.right = helper(A, middle + 1, end)

    return x


def level(node: TreeNode):
    queue = deque()
    queue.append(node)
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            print(node.key, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print(" ")


def main():
    x = minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    level(x)


if __name__ == "__main__":
    main()
