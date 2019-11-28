x = 5
x = 'Gopal'

class PyCharm:
    def execute(self):
        print("compiling")
        print("running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = PyCharm()

lap = Laptop()
lap.code(ide)
