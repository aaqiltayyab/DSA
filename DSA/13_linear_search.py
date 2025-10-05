def linear_search(arr, target):
    n = len(arr)
    ans = -1
    for i in range(n):
        if arr[i] == target:
            ans = i
            return ans
    return ans
arr = [10, 20, 5, 25, 15]
target = 25
result = linear_search(arr, target)
print(result)
