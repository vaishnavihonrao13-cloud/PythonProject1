class emp:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def input(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name", self.name)
        print("age", self.age)


e1 = emp()
e2 = emp()
e1.input("Vaishnavi", 21)
e1.display()
e2.display()