class organisation:
    def __init__(self):
        self.inner1 = self.department1()
        self.inner2 = self.department2()

    def showname(self):
        print("organisation : fct")

    class department1:
        def dispdept1(self):
            print("department 1")

    class department2:
        def dispdept2(self):
            print("department 2")


outer = organisation()
outer.showname()

inner1 = outer.inner1
inner2 = outer.inner2

inner1.dispdept1()
inner2.dispdept2()