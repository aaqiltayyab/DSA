a, b = 0, 1
n = int(input("Enter the number : "))
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#fibonacci Quiz
n = int(input("Enter the number : "))
f = [0]*(n+1)
f[0] = 0
f[1] = 1
for i in range(2,n+1):
    f[i] = f[i-1] + f[i-2]
print(f[n])

#fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the number : "))
print(fibonacci(n))



