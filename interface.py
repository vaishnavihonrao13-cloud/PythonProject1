from abc import ABC, abstractmethod
class demointerface(ABC):
    @abstractmethod
    def method1(self):
        print("Method 1")
        return
    @abstractmethod
    def method2(self):
        print("Method 2")
        return
class concreteclass(demointerface):
    def method1(self):
        print("Method ")
        return
    def method2(self):
        print("Method 2")
        return
obj = concreteclass()
obj.method1()
obj.method2()
