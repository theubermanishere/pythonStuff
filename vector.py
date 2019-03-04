class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Returns jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):     # relies on __len__ method
            raise ValueError('dimension must agree')
        result = Vector(len(self))      # init a new vector
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

    def __str__(self):
        """Produce string representation"""
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == '__main__':
    n = 3
    v = Vector(n)
    for i in range(n):
        v[i] = i

    w = Vector(n)
    for i in range(n):
        w[i] = i * i

    print("Vector v: ", v)
    print("Vector w: ", w)
    print("Sum: ", v+w)
    print("Equality Check: ", v == w)

