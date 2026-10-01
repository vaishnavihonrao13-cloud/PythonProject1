# inner class is class with in  another class.

class student:
    def __init__(self):
        self.name = "Anish"
        self.sub = self.Subject()

    def show(self):
        print("Name:", self.name)
        self.sub.display()

    class Subject:
        def __init__(self):
            self.sub1 = "Java"
            self.sub2 = "Python"

        def display(self):
            print(self.sub1)
            print(self.sub2)


s = student()
s.show()