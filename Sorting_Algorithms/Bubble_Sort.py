def bubble_sort(arr):
    # Defining bubble sort fcn that takes list input
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then the array is sorted
        if not swapped:
            break
            
    return arr

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original Unsorted: ", data)
    sorted_data = bubble_sort(data)
    print("Sorted Data:", sorted_data)