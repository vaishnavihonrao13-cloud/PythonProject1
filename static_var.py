class Employee:
    'optional class documentation string that will help to understand the purpose of class'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def showCount():
        print("Total Employees ", Employee.empCount)
        return

    counter = staticmethod(showCount)

    def displayEmp(self):
        print("Name := " + self.name, " Salary := ", self.salary)


emp1 = Employee("Dinesh", 40000)
emp2 = Employee("Harsh", 30000)
emp3 = Employee("Payal", 45000)

emp1.counter()
Employee.counter()