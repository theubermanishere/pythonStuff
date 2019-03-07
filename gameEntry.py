class GameEntry:
    """Represents one entry of a list of high scores."""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with the given capacity."""

        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        """Return kth entry."""
        return self._board[k]

    def __str__(self):
        """Return string representation."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Consider adding entry to the high scores."""
        score = entry.get_score()

        # Does the new entry qualify as a high score?
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry


