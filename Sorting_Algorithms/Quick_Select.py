import time
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
    #Recursive Quick Select
    
    if low  <= high:
        pi = partition(arr, low, high)
        if pi == k: 
            return arr[pi]
        elif pi > k: 
            return quick_select(arr, low, pi-1, k)
        else: 
            return quick_select(arr, pi+1, high, k)
        
def timed_quick_select(arr: List[int], k: int) -> int:
    
    start= time.perf_counter()
    result = quick_select(arr, 0, len(arr)-1, k)
    end = time.perf_counter()
    print(f"[QuickSelect] found k={k} in {end-start:.6f} sec")
    return result 

#DEMO the example
incomes = [50000, 72000, 48000, 93000, 60000, 83000, 75000]
median_idx = len(incomes) // 2 
median_income = timed_quick_select(incomes, median_idx)
print("Median income:", median_income)
    
                
        