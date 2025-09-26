# Quick Sort ALgorithm: in-place, Unstable
# Time: Average: O(n log n), Worst: O(n^2)

def quick_sort(arr):
    
    def partition(low, high):
        pivot = arr[(low + high) // 2]  # middle element pivot
        i, j = low, high 
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return i, j     # i = first index of right partition; j = last of left 

    def sort(low, high):
        if low < high:
            i, j = partition(low, high)
            sort(low, j)
            sort(i, high)   
                 
    sort(0, len(arr) - 1)
    return arr  