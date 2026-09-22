class person:
    def __init__(self,name):
        self.name=name
class employee(person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id
class manager(employee):
    def __init__(self,name,emp_id,dept):
        super().__init__(name,emp_id)
        self.dept=dept
m=manager("Vaishanavi",1,"it")
print(m.name)
print(m.emp_id)
print(m.dept)