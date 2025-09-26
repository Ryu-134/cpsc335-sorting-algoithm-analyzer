# Merge Sort Algorithm: in-place, stable
# Time: Always -> O(n log n)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # copy left half
    right_half = merge_sort(arr[mid:])  # copy right half

    merged = merge(left_half, right_half)   
    arr[:] = merged     # act in-place to run benchmark
    return arr 

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right): # linear merge; stable as taken from left given a tie
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result