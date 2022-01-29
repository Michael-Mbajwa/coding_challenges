"""
Given a linked list, rearrange the node values such that they appear in alternating
low ➔ high ➔ low ➔ high ➔ ... form.
For example,given 1 ➔ 2 ➔ 3 ➔ 4 ➔ 5,you should return 1 ➔ 3 ➔ 2 ➔ 5 ➔ 4.
"""
# Implementation of the challenges begins on line 138


# Linked lists
class Node:
    """
    A class for a singly LinkedList with a pointer to the next Node.
    """
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, _data):
        self.data = _data

    def set_next(self, _next):
        self.next = _next


class LinkedList:
    """
    Implementation of an unordered LinkedList.
    """
    def __init__(self, item=None):
        if item is None:
            self.head = None
        else:
            self.head = Node(item)

    def is_empty(self):
        return self.head is None

    def prepend(self, item):
        """
        Adds item to the LinkedList
        :param item: item to be added
        :return: None
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        :return: The number of items in the list.
        """
        count = 0
        walk = self.head
        while walk is not None:
            walk = walk.get_next()
            count += 1
        return count

    def search(self, item):
        """
        :param item: Item whose presence we are checking in the LinkedList
        :return: True if the item exists, false otherwise.
        """
        current = self.head
        found = False
        while not found and current is not None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def append(self, item):
        """
        The logic of the LinkedList is that the most recent item to be added is the head. Append on the other hand
        adds any item at the end of the LinkedList. For example appending a LinkedList with this structure:
        2->9->6->3->5 will lead to 2->9->6->3->5->new_item
        :param item: Item to be added at the ending of the LinkedList
        :return: Nothing
        """
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(Node(item))

    def tail(self):
        """
        :return: The last item in the chain
        """
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()

        return current.get_data()

    def get_head(self):
        """
        :return: Returns the head of the LinkedList
        """
        return self.head

    def remove(self, item):
        if item == self.head.get_data():
            self.head = self.head.get_next()
        else:
            found = False
            current = self.head
            prev = self.head
            while not found and current is not None:
                if current.get_data() == item:
                    found = True
                else:
                    prev = current
                    current = current.get_next()
            if current is None:
                return "Item does not exist."
            else:
                prev.set_next(current.get_next())

    def print_elements(self):
        """
        :return: A list showing how the items in the LinkedList are arranged.
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.get_data())
            current = current.get_next()
        return result


# Implementation of the challenges
def high_low_linked_list(ll):
    """
    Given a linked list, rearrange the node values such that they appear in alternating
    low ➔ high ➔ low ➔ high ➔ ... form.
    For example,given 1 ➔ 2 ➔ 3 ➔ 4 ➔ 5,you should return 1 ➔ 3 ➔ 2 ➔ 5 ➔ 4.
    :param ll:
    :return:
    """
    check = True  # For low -> high
    curr = ll

    while curr.get_next():
        if curr.get_next().get_data() < curr.get_data() and check:  # L->h situation and current is less than previous
            temp = curr.get_data()
            curr.set_data(curr.get_next().get_data())
            curr.get_next().set_data(temp)

        elif curr.get_data() < curr.get_next().get_data() and not check:  # h->l situation and prev is less than current
            temp = curr.get_data()
            curr.set_data(curr.get_next().get_data())
            curr.get_next().set_data(temp)

        check = not check
        curr = curr.get_next()

    return ll


if __name__ == "__main__":
    ll1 = LinkedList(5)
    ll1.prepend(4)
    ll1.prepend(3)
    ll1.prepend(1)
    ll1.prepend(2)
    node1 = ll1.get_head()
    current = high_low_linked_list(node1)
    while current is not None:
        print(current.get_data())
        current = current.get_next()