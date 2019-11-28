#using for else loop we can do this
num = 13
for i in range(2,num):
    if num % i == 0:
        print("Not Pime")
        break
else:
    print("Prime")