from array import *
# array(typecode, arr) i = signed intiger i.e  minus value can be taken, I= unsigned intiger i.e only plus value can be taken
vals = array('i',[5,6,4,3,1])
for i in vals:
    print(i)

print("Bye")


#------------------------------------------
arr = array('i',[])
len  = int(input("Please enter the quantity: "))
for i in range(len):
    n = int(input("Enter a no. :"))
    arr.append(n)

print(arr)

print("Bye")