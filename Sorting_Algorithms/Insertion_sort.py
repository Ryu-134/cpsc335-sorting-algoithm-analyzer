# Insertion Sort Algorithm: in-place, stable
# Time: Best: O(n), Average/Worst: O(n^2)

def insertion_sort(arr):    
    for i in range(1, len(arr)):    # build sorted prefix
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:  # shift larger elements right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key    # insert key
    return arr