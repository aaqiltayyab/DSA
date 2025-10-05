#Question 
#input = 5 3
#input = -2 0 5 -1 -3
#output = 11

def max_sum(arr, k):
    n = len(arr)
    sorted_arr = sorted(arr)
    for i in range(n):
        if sorted_arr[i] < 0 and 0 < k:
            sorted_arr[i] = -sorted_arr[i]
            k -= 1
    return sum(sorted_arr)

n, k = map(int, input("Enter the number of elements : ").split())
arr = list(map(int,input("Enter the elements : ").split()))
result = max_sum(arr,k)
print(result)

