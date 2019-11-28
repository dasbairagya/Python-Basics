# def hello():
#     print("hello")
# hello()


def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d
res1, res2 = add_sub(10,5)
print(res1,res2)

def add(x,y):
    c = x+y
    return c


a = int(input("Enter a no : "))
b = int(input("Enter another no : "))
res = add(a,b)
print("Sum of the nos. is: ",res)
