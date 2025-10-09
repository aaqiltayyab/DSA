v = ["a","e","i","o","u"]
s = input("Enter the string : ")
c = 0
for i in s:
    if i.lower() in v:
        c += 1
print("Number of vowels in the string is : ",c)
