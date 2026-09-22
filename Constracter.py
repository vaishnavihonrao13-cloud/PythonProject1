class Student:
    def __init__(self):
        print("No argument constructor")

    def __init__(self, name="unkown", age=0):
        self.name = name
        self.age = age
        self.password='1234'#__password
        print("Parameterized constructor")
s3=Student()
s1 = Student("Vaishnavi", 21)
s2 = Student("Siddhi", 21)
print(s3.name, s3.age,s3.password)
print(s1.name, s1.age)
print(s2.name, s2.age)
