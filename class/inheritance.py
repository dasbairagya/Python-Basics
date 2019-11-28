






class A:
    def __init__(self):
        print("init from class A")

    def feature1(self):
        print("this is feature 1 from class A \n")


class B:
    def __init__(self):
        print("init form class B \n")

    def feature2(self):
        print("this is feature 2 from class B \n")

#single level inheritance
class C(A):
    def __init__(self):
        print("init from class C")
        # call the init method of parent class
        super().__init__()

    def feature3(self):
        print("this is feature 3 from class C")

#multi level inheritance
class D(A,B):
    def __init__(self):
        print("init from class D")
        #MRO(method resolution order)
        super().__init__() #it call init of class A but not B because it goes from left to right

    def feature4(self):
        print("this is feature 4 from class D")
        super().feature2() #call the feature2() from class B






obj1 = A()
obj1.feature1()

obj2 = B()
obj2.feature2()

obj3 = C()
obj3.feature1()

obj4 = D()
obj4.feature1()
obj4.feature2()
obj4.feature4()

