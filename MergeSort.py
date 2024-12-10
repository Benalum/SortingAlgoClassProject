def three_way_merge_sort(arr, start_location_size, one_third_size_location, two_third_size_location,
                          end_location_size, d_arr):
    # Get the index location for the 0/3 , 1/3, 2/3, 3/3.
    i = start_location_size
    j = one_third_size_location
    k = two_third_size_location
    l = start_location_size

    # Sorting first iteration chose the smallest in the three ranges
    while i < one_third_size_location and j < two_third_size_location and k < end_location_size:
        # Check to see if the value at i is less than j
        if arr[i] < arr[j]:
            if arr[i] < arr[k]:
                d_arr[l] = arr[i]
                l += 1
                i += 1
            else:
                d_arr[l] = arr[k]
                l += 1
                k += 1
        # If statement fails then we know index j of array arr is less than index i of array arr
        else:
            if arr[j] < arr[k]:
                d_arr[l] = arr[j]
                l += 1
                j += 1
            else:
                d_arr[l] = arr[k]
                l += 1
                k += 1

    # Sorting second iteration: Remaining values for first and second range.
    while i < one_third_size_location and j < two_third_size_location:
        if arr[i] < arr[j]:
            d_arr[l] = arr[i]
            i += 1
            l += 1
        else:
            d_arr[l] = arr[j]
            l += 1
            j += 1

    # Sorting third iteration: Remaining values second to third range.
    while j < two_third_size_location and k < end_location_size:
        if arr[j] < arr[k]:
            d_arr[l] = arr[j]
            j += 1
            l += 1
        else:
            d_arr[l] = arr[k]
            l += 1
            k += 1

    # Sorting fourth iteration: Remaining values for third and first range.
    while i < one_third_size_location and k < end_location_size:
        if arr[i] < arr[k]:
            d_arr[l] = arr[i]
            i += 1
            l += 1
        else:
            d_arr[l] = arr[k]
            l += 1
            k += 1

    # Copy remaining values from the first range
    while i < one_third_size_location:
        d_arr[l] = arr[i]
        l += 1
        i += 1

    # Copy remaining values from the second range
    while j < two_third_size_location:
        d_arr[l] = arr[j]
        l += 1
        j += 1

    # Copy remaining values from the third range
    while k < end_location_size:
        d_arr[l] = arr[k]
        l += 1
        k += 1

    return d_arr


# Merge function
def three_way_merge_sort_split(d_arr, start_location_size, end_location_size, arr):
    size = end_location_size - start_location_size

    # Check size return if < 2
    if end_location_size - start_location_size < 2:
        return

    # Since this is a three-way merge sort, we must split the array into 3 separate sections
    one_third_size_location = start_location_size + (size // 3)
    two_third_size_location = start_location_size + 2 * (size // 3) + 1  # Prevents maximum recursion doing + 1

    # Recursively split the array.
    three_way_merge_sort_split(arr, start_location_size, one_third_size_location, d_arr)
    three_way_merge_sort_split(arr, one_third_size_location, two_third_size_location, d_arr)
    three_way_merge_sort_split(arr, two_third_size_location, end_location_size, d_arr)

    # Merge to create the sorted array
    three_way_merge_sort(arr, start_location_size, one_third_size_location, two_third_size_location,
                         end_location_size, d_arr)


# Check if size exists, create a duplicate array
def three_way_merge_sort_initialization(arr):
    size = len(arr)

    # Create a duplicate array
    d_arr = arr.copy()

    # Run the first function for three-way merge sort which would be splitting the array into 1/3 sections.
    three_way_merge_sort_split(d_arr, 0, size, arr)

    arr = d_arr.copy()

    return arr
