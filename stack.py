class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Stack:
    """LIFO Stack implemented using Python list."""

    def __init__(self):
        """Empty stack init."""
        self._data = []

    def __len__(self):
        """Return the no of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return the top element without removing it."""
        if self._is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove the top element and return it."""
        if self._is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()
