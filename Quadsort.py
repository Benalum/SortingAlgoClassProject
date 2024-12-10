import time

def heapify(arr, N, i):
    largest = i
    children = {}

    # Determine if the key of any of the four children of i are larger than the key of i
    for j in range(4):
        children[j] = 4 * i + j + 1
        if children[j] < N and arr[largest] < arr[children[j]]:
            largest = children[j]

        # if the key of any of the four children of i is larger than the key of i,
        # swap the keys of the child and the parent
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

         # run heapify on the root of the swapped child
        heapify(arr, N, largest)

# heapSort: Sorts an array of given size using a quad-degree max-heap.
# input: an unsorted array
# output: the corresponding sorted array
def heapSort(arr):
    N = len(arr)

    # Build the quad-degree maxheap.
    for i in range(N//4 - 1, -1, -1):
        heapify(arr, N, i)

    # iteratively extract the first element from the front of the max-heap,
    # then run heapify on the array less the last element
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
    return arr