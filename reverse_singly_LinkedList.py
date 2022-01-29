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


class DoubleNode:
    """
    A class for a doubly LinkedList with pointers to the previous and next Node.
    """
    def __init__(self, data, _next=None, prev=None):
        self.data = data
        self.next = _next
        self.prev = prev

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, _data):
        self.data = _data

    def set_next(self, _next):
        self.next = _next

    def set_prev(self, _prev):
        self.prev = _prev


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


def reversed_linked_list(head):
    """
    Given the head of a singly LinkedList, reverse it in-place.
    :param head: head of linked list to be reversed
    :return:
    """
    if head is None:  # The case where the LinkedList is empty
        return None
    if head.get_next() is None:  # Situation where the LinkedList contains only one item
        return head

    # A singly linked list follows this logic: 2->9->6->3->5->None. To reverse it, we could instead simply make each
    # node point to the element before it. None<-2<-9<-6<-3<-5 == 5->3->6->9->2->None

    prev, _current = None, head

    while _current is not None:
        temp = _current.get_next()
        _current.set_next(prev)
        prev = _current
        _current = temp

    return prev


if __name__ == "__main__":
    ll = LinkedList(5)
    ll.prepend(3)
    ll.prepend(6)
    ll.prepend(9)
    ll.prepend(2)
    head = ll.get_head()
    reversed_ll = reversed_linked_list(head)
    current = reversed_ll
    while current is not None:
        print(current.get_data())
        current = current.get_next()