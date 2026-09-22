class emp:
    'optional class documentation string that will help to understand this class purpose'
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        emp.empCount+=1
    def displayCount(self):
        print("total employees",emp.empCount)

    def displayEmployee(self):
        print("employee name",self.name)
        print("employee salary",self.salary)
em1=emp("",20000)
em1.displayEmployee()
print(emp.empCount)
print("emp.__doc__",emp.__doc__)