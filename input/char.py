#taking  multiple charactors as an input and print as required
name = input("Enter your name: ")
print('Hello ' + name +' first letter of your name is :' + name[0])

#taking a single specific char form multiple charactors as an input and print the same
name  = input("Enter your name: ")[0]
print (' first letter of your name is :' + name)
#taking an expression (e.g. 6+2-1) as an input and print the result
result = eval(input("Enter an Expression: "))
print(result)