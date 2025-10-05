n = int(input("Enter the number : "))
if n > 1:
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

#prime number another aproach
n = int(input("Enter the number : "))
isPrime = True
if n <= 1:
    isPrime = False
else:
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            isPrime = False
            break
if isPrime:
    print("Prime number")   
