class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize the Range instance."""

        if step == 0:
            raise ValueError('Step cannot be 0')

        if stop is None:
            start, stop = 0, start

        # calculate the length once
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        """Return the length of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return the kth entry."""

        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

if __name__ == '__main__':
    oneToFour = Range(4)

    for i in oneToFour:
        print(i)

    for i in Range(5):
        print(i)
