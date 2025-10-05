def push_all_zeros_to_the_end(arr):
    n = len(arr)
    count = 0
    temp = [0]*n
    for i in range(n):
        if arr[i] != 0:
            temp[count] = arr[i]
            count += 1

    while count < n:
        temp[count] = 0
        count += 1

    return temp
arr = [0,1,9,8,0,0,7,0]
result = push_all_zeros_to_the_end(arr)
print(result)

# def push(arr):
#     arr.sort(key = lambda x : x == 0)
#     return arr
# arr = [0,1,9,8,0,0,7,0]
# print(push(arr))
