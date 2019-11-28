a = 5  #101 -- 3 bits
b = 6  #110
#using third variable
temp = a
a = b
b = temp
print(a)
print(b)
#without using third variable
a = a + b # 11 -- 4 bits hence wasting 1 extra bit hence use XOR
b = a - b
a = a - b
print(a)
print(b)
#using XOR
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)

#using unic method of python not other languages
# search rot_two in google, you will get the idea how it works
a,b = b,a
print(a)
print(b)