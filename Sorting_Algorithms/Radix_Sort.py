#Radix Sort (LSD) that will support non negative integers directly.
#providing wrapper to handle negatives as well
#Demo of a real world scenario - sorting order records by order_id

from typing import List, Dict, Tuple
import time 
import random

# Core: stable counting sort by one digit (base would be 10 by default) 

def _counting_sort_by_digit(a: List[int], exp: int, base: int = 10) -> None:
    n = len(a) 
    output = [0] * n
    count = [0] * base
    
    #1 Count occurences of this digit among all #s 
    for i in range(n): 
        digit = (a[i] // exp) % base
        count[digit] += 1 
    
    #2 Prefix Sums: transform counts into ending positions
    for d in range(1, base):
        count[d] += count[d - 1]
        
    #3 Stable write: traverse input backwards to preserve the order of equal digits
    for i in range(n - 1, -1, -1):
        digit = (a[i] // exp) % base
        pos = count[digit] - 1
        output[pos] = a[i]
        count[digit] -= 1
        
    #4 Copy back: make this pass's result become the new array for the next digit 
    for i in range(n):
        a[i] = output[i]
        
#Define Radix Sort LSD for Non Negative Integers
def radix_sort_lsd_nonneg(a: List[int], base: int = 10) -> List[int]:
    if not a:
        return a

    start = time.perf_counter() #Starting high resolution tier for benchmarking
    
    max_val = max(a)
    exp = 1 
    while max_val // exp > 0:
        _counting_sort_by_digit(a, exp, base)
        exp *= base 
        
    end = time.perf_counter()
    print(f"[Radix] nonneg sort in {end - start:.6f} sec (base={base})")
    return a

#Handling negative value
def radix_sort_lsd(a: List[int], base: int = 10) -> List[int]:
    if not a:
        return a

    neg = [-x for x in a if x < 0] 
    pos = [x for x in a if x >= 0] 
    
    #Sort both subset
    if neg:
        radix_sort_lsd_nonneg(neg, base)
    if pos: 
        radix_sort_lsd_nonneg(pos, base)
        
    neg_sorted = [-x for x in reversed(neg)]
    
    out = neg_sorted + pos
    return out

#Real world scenario- Sorting Order Records
def sort_orders_by_id(orders: List[Dict], key: str = "order_id", base: int = 10) -> List[Dict]:
    if not orders:
        return orders
    
    keys = []
    indx = []
    
    for i, rec in enumerate(orders): 
        keys.append(int(rec[key]))
        indx.append(i)
        
    def stable_pass_with_companion(keys: List[int], comp: List[int], exp: int, base: int) -> None:
        n = len(keys)
        out_keys = [0] * n
        out_comp = [0] * n 
        count = [0] * base 
        for i in range(n):
            d = (keys[i] // exp) % base
            count[d] += 1
        for d in range(1, base):
            count[d] += count[d - 1]
        for i in range(n - 1, -1 , -1):
            d = (keys[i] // exp) % base
            pos = count[d] - 1 
            out_keys[pos] = keys[i]
            out_comp[pos] = comp[i]
            count[d] -= 1
        for i in range(n):
            keys[i] = out_keys[i] 
            comp[i] = out_comp[i]
            
    #Run LSD Passes
    max_key = max(keys)
    exp = 1
    start = time.perf_counter()
    while max_key // exp > 0:
        stable_pass_with_companion(keys, indx, exp, base)
        exp *= base
    end = time.perf_counter()
    print(f"[Radix] order sort in {end - start:.6f} sec for {len(orders)} records")
    
    sorted_orders = [orders[i] for i in indx]
    return sorted_orders
                
