import random

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i + 1

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def randomized_quick_sort(A):
    stack = [(0, len(A)-1)]

    while stack:
        p, r = stack.pop()
        if p < r:
            q = randomized_partition(A, p, r)
            # Pushing smaller range first to minimize stack use
            if q - 1 - p < r - (q + 1):
                stack.append((q + 1, r))
                stack.append((p, q - 1))
            else:
                stack.append((p, q - 1))
                stack.append((q + 1, r))
    return A