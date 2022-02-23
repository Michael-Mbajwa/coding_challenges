class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


def palindrome_linked_list(root):
    """
    This problem was asked by Google.

    Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

    For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
    :param root:
    :return:
    """
    if not root:
        return None

    result = ""

    while root:
        result += str(root.data)
        root = root.nxt

    print(result)
    print(result[::-1])

    if result == result[::-1]:
        return True

    return False


if __name__ == "__main__":
    root = Node(4)
    root.nxt = Node(4)
    root.nxt.nxt = Node(3)
    root.nxt.nxt.nxt = Node(4)
    root.nxt.nxt.nxt.nxt = Node(4)
    print(palindrome_linked_list(root))