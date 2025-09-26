# Bucket Sort Algorithm: in-place, stable (as equal buckets go to same bucket and python timsort is stable)
# Time: Average: O(n + k), Worst: O(n^2)


def bucket_sort(arr):    
    n = len(arr)
    if n == 0:
        return arr
    
    buckets = [[] for _ in range(n)]     # create n empty buckets 
    mn, mx = min(arr), max(arr)
    span = mx - mn if mx != mn else 1   # avoid divide by zero if all equal

    for x in arr:   # distribute into buckets by normalized index and clamp max element to last bucket
        idx = int((x - mn) * n / span)
        if idx == n:       
            idx = n - 1
        buckets[idx].append(x)
    
    for b in buckets:   # sort each bucket via timsort
        b.sort()
        
    output = []
    for b in buckets:
        output.extend(b)
    arr[:] = output #NOTE: copy merged result into arr via shallow copy to act in-place for timing
    return arr
        

