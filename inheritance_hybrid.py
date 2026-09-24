class person:

    def show_person(self):
        print("person show")


class student(person):

    def show_student(self):
        print("student show")


class teacher(person):

    def show_teacher(self):
        print("teacher show")


class assistant(student, teacher):

    def show_assistant(self):
        print("assistant show")


a = assistant()

a.show_person()
a.show_student()
a.show_teacher()
a.show_assistant()