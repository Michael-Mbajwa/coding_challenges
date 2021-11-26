class Graph:
    """
    A class created for an undirected graph.
    The graph class uses a dict-of-dict data structure.
    A graph stores vertices and edges. Edges are undirected but can be weighted.
    This graph supports parallel edges.

    The outer dict (vertices_dict) holds information keyed by vertex.
    The inner dict holds edge data keyed by each neighbor.

    """

    def __init__(self, data=None):
        """
        :param data: The graph class can be created with a value for the vertex. data must be hashable.
        """
        self.nodes = {}
        try:
            if data is not None:
                self.nodes[data] = {}
        except TypeError:
            print('Please provide an number or a string instead.')

    def __getitem__(self, item1, item2=None):
        if item2:
            return self.nodes[item1][item2]
        else:
            return self.nodes[item1]

    def __contains__(self, item):
        """Returns True if item is a node on the graph"""
        try:
            return item in self.nodes
        except TypeError:
            return False

    def __len__(self):
        """Returns the length of the number of vertices in the graph."""
        return len(self.nodes)

    def add_vertex(self, item):
        """
        :param item: Because we are using a dictionary structure, item has to be hashable. That means it can be any
        data structure except None. Our node can be an integer, float, string etc.
        """
        try:
            if item not in self.nodes:
                self.nodes[item] = {}
            else:
                pass
        except TypeError:
            print('Please provide an number or a string instead.')

    def number_of_vertices(self):
        """
        :return: the number of nodes in the graph.
        """
        return len(self.nodes)

    def add_edge(self, u, v, label=None):
        """
        Adds an edge between vertices u and v
        :param u: Must be provided. If u doesn't exist, it will be created
        :param v: Must be provided. If v doesn't exist, it will be created
        :param label: Refers to the name of the edge. Default value is None.
        """
        if u not in self.nodes:
            self.nodes[u] = {}
        if v not in self.nodes:
            self.nodes[v] = {}

        # create the edge
        if label:
            self.nodes[u][v] = label
            self.nodes[v][u] = label
        else:
            self.nodes[u][v] = str(u) + str(v)
            self.nodes[v][u] = str(u) + str(v)

    def vertices(self):
        """
        :return: A set of vertices in the graph
        """
        data = set()
        for key in self.nodes.keys():
            data.add(key)
        return data

    def edges(self):
        """
        Returns the set of edges of the graph.
        :return:
        """
        edges = []

        for vertex in self.nodes.keys():
            for adj in self.nodes[vertex].keys():
                edge_list = sorted([vertex, adj])
                if edge_list not in edges:
                    edges.append(edge_list)
                else:
                    pass

        return edges

    def is_edge(self, u, v):
        """
        Checks if an edge exists
        :param u: first vertex
        :param v: second vertex
        :return: True if the edge exists else return a statement saying it doesnt exist.
        """
        if sorted([u, v]) in self.edges():
            return True
        else:
            return 'This edge does not exist'

    def deg(self, v):
        """
        Degree is the number of edges adjacent to a vertex.
        :param v: the vertex we are interested in getting the degree
        :return:
        """
        # first check if the vertex exists
        if v not in self.nodes:
            return 'This vertex does not exist. Use the add_vertex method to add a vertex.'
        else:
            degree = len(self.nodes[v].values())
            return degree


# To test the graph class, we can create a simple graph
if __name__ == '__main__':
    g = Graph()
    g.add_edge('a', 'b', label='ab')
    g.add_edge('a', 'd')
    g.add_edge('b', 'd')
    g.add_edge('c', 'b')
    print(len(g))
    print(g.number_of_vertices())
    print(g.vertices())
    print(g.edges())
    print(g.deg('b'))
    print(g.is_edge('b', 'a'))
    print(g.nodes)
    print(g['a']['b'])


# Implementation of a stack ADT
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Checks to see if stack is empty or not.
        :return: True if stack is empty. False otherwise.
        """
        return self.items == []

    def push(self, item):
        """
        Inserts an item at the top of the stack. In this case, the end of the list.
        :param item: Value to be added.
        :return: Nothing.
        """
        self.items.append(item)

    def pop(self):
        """
        Returns the last item in the stack which is the most recently addded. This is because the stack uses the
        first in first out logic.
        :return:
        """
        return self.items.pop()

    def peek(self):
        """
        To be used to view the most recently added item.
        :return: Returns the last element in the stack.
        """
        return self.items[-1]

    def size(self):
        """
        Checks the number of items in the stack.
        :return: Returns a number.
        """
        return len(self.items)


class Queue:
    def __init__(self):
        """
        A queue uses a first in first out logic. That means, items that appeared first are removed first.
        """
        self.items = []

    def is_empty(self):
        """
        Checks to see if the queue is empty
        :return: True: if queue is empty. False: Otherwise
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Adds an item to the queue.
        :param item: Value to be added to the queue.
        :return: No value is added.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove the first item on the queue
        :return:
        """
        return self.items.pop(0)

    def peek(self):
        """
        View the first item on the list
        :return:
        """
        return self.items[0]

    def __len__(self):
        return len(self.items)


# Implementation of a Deque
class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        self.items.pop()

    def remove_rear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)


# Implementation of a linked list - Ordered and Unordered
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks to see if the LinkedList is empty or not.
        :return: True if it is empty and False otherwise.
        """
        return self.head is None

    def add(self, item):
        """
        Adds an item to the linkedList
        :param item: Item to be added to the linkedlist
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        :return: The number of items in the LinkedList
        """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)


# Implementing a Map abstract data type using a HashTable
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] == data  # replaces old data

            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)