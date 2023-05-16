def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Example usage:
array = [9, 2, 5, 1, 7, 6, 8, 3, 4]
sorted_array = quicksort(array)
print("Sorted array:", sorted_array)
