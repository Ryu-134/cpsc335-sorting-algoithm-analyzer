# Radix Sort (LSD) + wrapper to handle negatives: in-place, stable 
# Time: Always -> O(d*(n+k))
    # n: total # of elements  d: # of digits in largest element of input array  k: base of number system

from typing import List


def _counting_sort_by_digit(a: List[int], exp: int, base: int = 10) -> None:
    n = len(a) 
    output = [0] * n
    count = [0] * base
    
    # count digit occurrence across all #s 
    for x in a: 
        count[(x // exp) % base] += 1   # integer division and modulo to extract the digits
    
    # prefix sums; store end positions
    for d in range(1, base):
        count[d] += count[d - 1]
        
    # stable write 
    for i in range(n - 1, -1, -1):
        digit = (a[i] // exp) % base
        pos = count[digit] - 1
        output[pos] = a[i]
        count[digit] -= 1
        
    # copy back
    a[:] = output
        
# for non-negative integers
def radix_sort_lsd_nonneg(a: List[int], base: int = 10) -> List[int]:
    if not a:
        return a    
    max_val = max(a)
    exp = 1 
    while max_val // exp > 0:
        _counting_sort_by_digit(a, exp, base)
        exp *= base 
    return a

# wrapper to allow handling of negative values
def radix_sort_lsd(a: List[int], base: int = 10) -> List[int]:
    if not a:
        return a
    
    neg = [-x for x in a if x < 0]  # split into negatives and non-negatives
    pos = [x for x in a if x >= 0] 
    
    # sort both subsets
    if neg:
        radix_sort_lsd_nonneg(neg, base)
    if pos: 
        radix_sort_lsd_nonneg(pos, base)        
    output = [-x for x in reversed(neg)] + pos    # merge back negatives ascending -> reverse of sorted abs values then pos
    a[:] = output
    return a

