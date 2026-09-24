class demointerface:
    def display(self):
        pass
class newclass(demointerface):
    def displayMsg(self):
        print("display method")
obj=newclass()
obj.displayMsg()