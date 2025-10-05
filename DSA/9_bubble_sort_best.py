def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swapped = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if swapped:
            break
    return arr
arr = [1,2,3,4,5]
result = bubble_sort(arr)
print(result)
