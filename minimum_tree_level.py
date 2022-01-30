from collections import defaultdict


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def smallest_level(root):
    """
    Get tree level with minimum sum
    Given a binary tree, return the level of the tree that has the minimum sum. The level of a node is defined as the number
    of connections required to get to the root, with the root having level zero.
    """
    storage = []  # We will use this to store a tuple of a node's data and the level it belongs to
    result = defaultdict(int)  # A dictionary for storing the sum of values in each level
    level = 0  # Initial root level is 0

    storage.append((root, level))  # The node is the first item, the level is the second
    while storage:  # While there is still data in the storage list, our loop continues
        val, level = storage.pop()  # Since each data is stored with its corresponding level, order doesn't matter.
        result[level] += val.data

        if val.left:
            storage.append((val.left, level+1))  # If left exists, we add to storage, and increase level by 1
        if val.right:
            storage.append((val.right, level+1))

    return min(result, key=result.get)


if __name__ == "__main__":
    root = Node(7)
    root.right = Node(3)
    root.left = Node(2)
    root.right.left = Node(4)
    root.right.right = Node(-5)
    print(smallest_level(root))