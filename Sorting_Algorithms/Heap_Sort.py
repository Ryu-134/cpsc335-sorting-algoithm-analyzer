# Heap Sort Algorithm: in-place, unstable
# Time: Always -> O(n log n)

def heap_sort(arr):

    def sift_down(a, start, end):
        root = start 
        while (left := 2 * root + 1) <= end:    # compute left (walrus operator) while checking the condition
            right = left + 1 
            largest = root
            if a[left] > a[largest]:
                largest = left
            if right <= end and a[right] > a[largest]:
                largest = right
            if largest == root:
                break
            a[root], a[largest] = a[largest], a[root]
            root = largest
    
    def build_max_heap(a):
        n = len(a)
        for i in range(n // 2 - 1, -1, -1): # start from last parent down to root
            sift_down(a, i, n - 1)
    
    a = arr
    n = len(a)
    build_max_heap(a)
    for end in range(n - 1, 0, -1): #repeatedly move max to end and restore heap
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end - 1)
    return a