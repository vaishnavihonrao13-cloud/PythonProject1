class organisation:
    def __init__(self):
        self.inner = self.department()

    def showname(self):
        print("organisation : fct")

    class department:
        def __init__(self):
            self.innerteam=self.team()
        def dispdept1(self):
            print("department")
        class team:
            def disptream(self):
                print("team : fct")
outer=organisation()
outer.showname()
dept=outer.inner
dept.dispdept1()

team = dept.innerteam
team.disptream()