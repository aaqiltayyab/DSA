def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            ans = mid
            right = mid - 1  # Continue left side for lower bound
        else:
            left = mid + 1
    return ans

arr = [1, 2, 3, 4, 4, 4, 7, 9, 11]
target = 4
result = binary_search(arr, target)
print(result)  # Output: -1 (Correct, kyunki 13 se bada ya barabar koi element nahi)
