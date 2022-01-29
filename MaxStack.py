# A more optimal solution
class MaxStack:
    """
    Implement a stack that has the following methods:
        • push(va1): push va1 onto the stack
        • pop: pop off and return the topmost element of the stack. If there are no elements in the stack,
        throw an error.
        • max: return the maximum value in the stack currently. If there are no elements in the stack, throw an error.
    Each method should run in constant time.
    """
    def __init__(self, data=None):
        if data:
            self.stack = [data]
            self._max = [data]
        else:
            self.stack = []
            self._max = []

    def push(self, val):
        """
        Appends item only to the end of the list
        :param val: new item
        :return:
        """
        self.stack.append(val)
        if self._max:
            self._max.append(max(val, self._max[-1]))  # Ensure
        else:
            self._max.append(val)

    def _pop(self):
        """
        :return: removes and returns the last item to be added
        """
        if self._max:
            self._max.pop()
        return self.stack.pop()

    def max_val(self):
        """
        :return: The last item that was added
        """
        return self._max[-1]


class Stack:
    """
    This problem was asked by Amazon.

    Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then
    it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it
    should throw an error or return null.

    Each method should run in constant time.
    """
    class Node:

        def __init__(self, element, next=None):
            self.value = element
            self.next = next

    def __init__(self, value=None):
        self.size = 0
        self.top = None
        self._max = None
        if value:
            self.top = self.Node(value)
            self.size += 1
            self._max = self.Node(value)

    def push(self, value):
        if self.top:
            self.top = self.Node(value, self.top)
            self.size += 1
            if value >= self._max.value:
                self._max = self.Node(value, self._max)
            else:
                holder = self._max
                while True:
                    if holder.next is None:
                        holder.next = self.Node(value)
                        break
                    elif value >= holder.next.value:
                        holder.next = self.Node(value, holder.next)
                        break
                    elif holder.next.value > value:
                        holder = holder.next
        else:
            self.top = self.Node(value)
            self.size += 1
            self._max = self.Node(value)

    def pop(self):
        if self.top:
            remove = self.top.value
            if remove == self._max.value:
                self._max = self._max.next
            else:
                holder = self._max
                while True:
                    if remove == holder.next.value:
                        holder.next = holder.next.next
                        break
                    else:
                        holder = holder.next

            self.top = self.top.next
            self.size -= 1
            return remove
        else:
            return None

    def topmost(self):
        if self.top:
            return self.top.value
        else:
            return None

    def length(self):
        return self.size

    def max(self):
        if self._max:
            return self._max.value
        else:
            return None


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(8)
    s.push(7)
    print(s.max())
    print(s.pop())
    print(s.max())
    print(s.pop())
    print(s.max())
    print(s.pop())
    print(s.max())
    print(s.pop())
    print(s.max())
