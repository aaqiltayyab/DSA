def lower_bound_linear_search(arr, t):
    n = len(arr)
    for i in range(n):
        if arr[i] >= t:
            return i
arr = [1,2,3,4,4,4,7,9,11]
t = 4
r = lower_bound_linear_search(arr, t)
print(r)