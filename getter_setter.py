class emp:
    def __init__(self):
        self.__salary=50000
    def get_salary(self):
        return self.__salary
    def set_salary(self, amount):
        if amount>0:
            self.__salary=amount
        else:
            print("invalid salary")
emp = emp()
print(emp.get_salary())
emp.set_salary(10000)
print(emp.get_salary())