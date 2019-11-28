from array import *
arr = array('i',[])
len  = int(input("Please enter the quantity: "))
for i in range(len):
    n = int(input("Enter a no. :"))
    arr.append(n)

print(arr)

src = int(input("Enter the value for search: "))
k = 0
for e in arr:
    if src==e:
        print("Index->",k)
        break
    k+= 1
else:
    print("Value not found")
print("Bye")