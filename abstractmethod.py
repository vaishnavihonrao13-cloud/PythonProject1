from abc import ABC,abstractmethod
class vechicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vechicle):
    def start(self):
        print("car")
class bike(vechicle):
    def start(self):
        print("bike")
c=car()
c.start()
b=bike()
b.start()