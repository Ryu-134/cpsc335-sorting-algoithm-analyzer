# Bubble Sort Algorithm: in-place, stable
# Time: Best: O(n), Average/Worst: O(n^2)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True        
        if not swapped:  # exit early if no swaps in this pass
            break            
    return arr
