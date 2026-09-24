class employee:
    def work(self):
        print("work")
class developer(employee):
    def code(self):
        print("code")
class manager(employee):
    def manage(self):
        print("manage")
m=manager()
m.work()
m.manage()
d=developer()
d.code()
d.work()