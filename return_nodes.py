class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def return_nodes(root):
    """
    This problem was asked by Microsoft.

    Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.
     1
    / \
   2   3
      / \
     4   5
    :param root: root of binary tree
    :return:
    """
    if not root:  # Return None if the tree is non existent
        return None

    stacks = [root]  # For storing leaves as we iterate through the tree
    result = []  # Stores our result

    while stacks:  # Code terminates once stacks is empty
        var = stacks.pop(0)
        result.append(var.data)

        if var.left:
            stacks.append(var.left)
        if var.right:
            stacks.append(var.right)

    return result


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(6)
    root.right = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.right = Node(1)
    root.right.left = Node(9)
    root.left.left.left = Node(11)
    root.left.left.left.left = Node(20)
    root.left.left.left.right = Node(13)
    root.right.left.left = Node(4)
    root.right.left.right = Node(10)

    print(return_nodes(root))