
#selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap only after the inner loop finishes
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [5, 8, 1, 3]
result = selection_sort(arr)
print(result)   # Output: [1, 3, 5, 8]
