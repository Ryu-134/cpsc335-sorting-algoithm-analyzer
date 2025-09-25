from typing import List

def bubble_sort(array, visualizer):
    """
    Implementation of the Bubble Sort algorithm.
    Yields the state of the array at each swap.
    """
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            visualizer.set_highlight([j, j + 1])
            yield True # Yield to allow for drawing

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                visualizer.set_highlight([j, j + 1])
                yield True # Yield to allow for drawing

        if not swapped:
            break
    visualizer.clear_highlight()
    return array

def insertion_sort(array, visualizer):
    """
    Implementation of the Insertion Sort algorithm.
    Yields the state of the array at each key insertion.
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        visualizer.set_highlight([i])
        yield True

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            visualizer.set_highlight([j + 1])
            yield True

        array[j + 1] = key
    
    visualizer.clear_highlight()
    return array

def selection_sort(array, visualizer):
    """
    Implementation of the Selection Sort algorithm.
    Yields the state of the array at each swap.
    """
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            visualizer.set_highlight([min_idx, j])
            yield True
            if array[j] < array[min_idx]:
                min_idx = j
        
        array[i], array[min_idx] = array[min_idx], array[i]
        visualizer.set_highlight([i, min_idx])
        yield True

    visualizer.clear_highlight()
    return array

def merge_sort(array, visualizer):
    """
    Generator for the Merge Sort algorithm.
    """
    yield from merge_sort_recursive(array, 0, len(array) - 1, visualizer)

def merge_sort_recursive(array, left, right, visualizer):
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort_recursive(array, left, mid, visualizer)
        yield from merge_sort_recursive(array, mid + 1, right, visualizer)
        yield from merge(array, left, mid, right, visualizer)

def merge(array, left, mid, right, visualizer):
    left_copy = array[left:mid + 1]
    right_copy = array[mid + 1:right + 1]

    i = 0  # Index for left_copy
    j = 0  # Index for right_copy
    k = left  # Index for merged array

    while i < len(left_copy) and j < len(right_copy):
        visualizer.set_highlight([k])
        yield True
        if left_copy[i] <= right_copy[j]:
            array[k] = left_copy[i]
            i += 1
        else:
            array[k] = right_copy[j]
            j += 1
        k += 1

    while i < len(left_copy):
        visualizer.set_highlight([k])
        yield True
        array[k] = left_copy[i]
        i += 1
        k += 1

    while j < len(right_copy):
        visualizer.set_highlight([k])
        yield True
        array[k] = right_copy[j]
        j += 1
        k += 1

    visualizer.clear_highlight()

def quick_sort(array, visualizer):
    """
    Generator for the Quick Sort algorithm.
    """
    yield from quick_sort_recursive(array, 0, len(array) - 1, visualizer)

def quick_sort_recursive(array, low, high, visualizer):
    if low < high:
        pi_generator = partition(array, low, high, visualizer)
        pi = yield from pi_generator
        
        yield from quick_sort_recursive(array, low, pi - 1, visualizer)
        yield from quick_sort_recursive(array, pi + 1, high, visualizer)

def partition(array, low, high, visualizer):
    pivot = array[high]
    i = low - 1
    visualizer.set_pivot(high)

    for j in range(low, high):
        visualizer.set_highlight([i, j])
        yield True
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            visualizer.set_highlight([i, j])
            yield True
    
    array[i + 1], array[high] = array[high], array[i + 1]
    visualizer.clear_highlight()
    visualizer.clear_pivot()
    return i + 1

# Heap Sort Generator
def heap_sort(array, visualizer):
    def sift_down(a, start, end):
        root = start 
        while (left := 2 * root + 1) <= end:
            right = left + 1 
            largest = root
            
            visualizer.set_highlight([root, left])
            if right <= end:
                visualizer.set_highlight([root, left, right])
            yield True 
            
            if a[left] > a[largest]:
                largest = left
            if right <= end and a[right] > a[largest]:
                largest = right
                
            if largest == root:
                break
            
            a[root], a[largest] = a[largest], a[root]
            visualizer.set_highlight([root, largest])
            yield True 
            root = largest
    
    def build_max_heap(a):
        n = len(a)
        for i in range(n // 2 - 1, -1, -1):
            yield from sift_down(a, i, n - 1)
    
    a = array
    n = len(a)
    yield from build_max_heap(a)
    
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        visualizer.set_highlight([0, end])
        yield True 
        
        yield from sift_down(a, 0, end - 1)
        
    visualizer.clear_highlight()
    return array

# Counting Sort Generator 
def counting_sort(array, visualizer):
    if not array:
        return array
    
    max_val = max(array)
    min_val = min(array)
    k = max_val - min_val + 1
    
    count = [0] * k 
    for i, num in enumerate(array):
        visualizer.set_highlight([i])
        yield True
        count[num - min_val] += 1
    
    output_temp = []
    
    output_index = 0
    for i, freq in enumerate(count):
        value = i + min_val
        for _ in range(freq):
            array[output_index] = value
            visualizer.set_highlight([output_index])
            yield True
            output_index += 1
            
    visualizer.clear_highlight()
    return array

# Bucket Sort Generator
def bucket_sort(array, visualizer):
    n = len(array)
    if n == 0:
        return array
    
    buckets = [[] for _ in range(n)]
    mn, mx = min(array), max(array)
    span = mx - mn if mx != mn else 1

    for i, x in enumerate(array):
        visualizer.set_highlight([i])
        yield True 

        idx = int((x - mn) * n / span)
        if idx == n:
            idx = n - 1
        buckets[idx].append(x)
    
    for i in range(n):
        buckets[i].sort() 

    k = 0
    for b in buckets:
        for x in b:
            array[k] = x
            visualizer.set_highlight([k])
            yield True 
            k += 1

    visualizer.clear_highlight()
    return array

# Generator for the counting sort pass to the radix function
def _counting_sort_by_digit_generator(a: List[int], exp: int, visualizer, base: int = 10):
    n = len(a)
    output = [0] * n
    count = [0] * base

    for i in range(n):
        visualizer.set_highlight([i])
        yield True

        digit = (a[i] // exp) % base
        count[digit] += 1

    for d in range(1, base):
        count[d] += count[d - 1]

    for i in range(n - 1, -1, -1):
        digit = (a[i] // exp) % base
        pos = count[digit] - 1
        output[pos] = a[i]
        count[digit] -= 1

        visualizer.set_highlight([i])
        yield True

    for i in range(n):
        a[i] = output[i]
        visualizer.set_highlight([i])
        yield True

# Radix Sort Generator
def radix_sort_lsd(array: List[int], visualizer):
    if not array:
        return array

    max_val = max(array)
    exp = 1

    while max_val // exp > 0:
        yield from _counting_sort_by_digit_generator(array, exp, visualizer)
        exp *= 10

    visualizer.clear_highlight()
    return array