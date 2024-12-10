def is_numerical_order(arr):
    # Check if the array is empty or has only one element
    if len(arr) <= 1:
        return True

    # Iterate through the array and compare adjacent elements
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False  # Array is not in numerical order

    return True  # Array is in numerical order
