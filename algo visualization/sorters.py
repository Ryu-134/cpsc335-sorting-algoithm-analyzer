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
