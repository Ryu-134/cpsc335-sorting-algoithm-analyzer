# Counting Sort Algorithm: in-place via copy back, stable
# Time: Always -> O(n + k)

# Works for integers as negatives handled by offsetting by min_val
def counting_sort(arr):
    n = len(arr)
    if n == 0:
        return arr
    
    min_val, max_val = min(arr), max(arr)   
    k = max_val - min_val + 1    # size of value range; offset = -min_val if min_val < 0 else 0
    
    count = [0] * k 
    for num in arr:     
        count[num - min_val] += 1
    
    # prefix sums; each bucket stores ending position
    for i in range(1, k):
        count[i] += count[i - 1]
    
    # stable write 
    output = [0] * n
    for i in range(n - 1, -1, -1):  # range reverse
        x = arr[i]
        count[x - min_val] -= 1
        output[count[x - min_val]] = x
    
    # copy back into arr (in-place) for benchmark
    arr[:] = output
    return arr