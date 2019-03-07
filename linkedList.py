class LinkedStack:
    """LIFO Stack implemented using a singly linked list."""

    # ------------ Nested Class --------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'     # more efficient memory usage

        def __init__(self, element, nextNode = None):
            self._element = element
            self._next = nextNode

    # ---------- Stack methods ---------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return number of element in the stack."""
        return self._size

    def is_empty(self):
        """Return True if stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return the value of the top element in the stack."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack."""

        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


class LinkedQueue:

    # ------------ Nested Class --------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'     # more efficient memory usage

        def __init__(self, element, nextNode = None):
            self._element = element
            self._next = nextNode

    # ---------- Stack methods ---------------
    class __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._empty
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
