def insertion_sort(L):
    """Sort list in nondecreasing order."""

    for k in range(1, len(L)):
        cur = L[k]
        j = k
        while j > 0 and L[j-1] > cur:
            L[j] = L[j-1]
            j -= 1
        L[j] = cur

if __name__ == '__main__':
    a = [1,7,2,4]
    insertion_sort(a)
    print(a)
