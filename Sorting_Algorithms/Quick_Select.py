# Quick Select Algorithm: in-place, not stable 
# Time: Average: O(n), Worst O(n^2) 

import random
from typing import List

def partition(arr: List[int], low: int, high: int) -> int:    
    pivot = arr[high] 
    i = low 
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quick_select(arr: List[int], low: int, high: int, k: int) -> int:
    if k < low or k > high:     # bounds + base case
        raise IndexError("k out of range")
    if low == high:
        return arr[low]
    
    pivot_index = random.randint(low, high)     # randomize pivot to avoid RecursionError
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    if low  <= high:
        pi = partition(arr, low, high)
        if pi == k: 
            return arr[pi]
        elif pi > k: 
            return quick_select(arr, low, pi-1, k)
        else: 
            return quick_select(arr, pi+1, high, k)
     