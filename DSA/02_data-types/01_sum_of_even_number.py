n = int(input("Enter the number : "))
s = 0
for i in range(n+1):
    if i % 2 == 0:
        s += i 
print("Sum of even number is : ",s)