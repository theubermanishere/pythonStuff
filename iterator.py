class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the sequence."""
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """Return the next element, or raise StopIteration"""
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

if __name__ == '__main__':
    sample_list = [1,2,3,4]
    iterator = SequenceIterator(sample_list)
    for i in iterator:
        print(i)
