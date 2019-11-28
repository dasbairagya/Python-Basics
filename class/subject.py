
#in python special variable or methods are decler as __methodName__


class Subject:
    #constractor as special method
    def __init__(self):
        self.name = "Math"
        self.price = 1000


    def favourite_sub(self, sub):
        print("my favourite subject is " + str(self.name) + " & " + sub + " & price is: $" + str(self.price))

book = Subject()
book.favourite_sub('English')