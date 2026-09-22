class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be positive")
        self._age = value


person = Person(30)

print(person.age)

person.age = 20
print(person.age)

