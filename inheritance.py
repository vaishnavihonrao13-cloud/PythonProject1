class parent:
    def parentmethod(self   ):
        print("parent method")
class child(parent):
    def childmethod(self):
        print("child method")
c=child()
c.parentmethod()
c.childmethod()
