def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element rightward
            j -= 1
        arr[j + 1] = key  # Place key in correct position
    return arr

arr = [12, -11, 136, 5, 6]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [1, 4, 5, 8, 9]
