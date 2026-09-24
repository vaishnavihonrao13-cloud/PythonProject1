from abc import ABC, abstractmethod
class scanable(ABC):
    @abstractmethod
    def scan(self):
        pass
class Printable(ABC):
    @abstractmethod
    def print_data(self):
        pass
class printerscanner(Printable,scanable):
    def scan(self):
        print("Scanning document")

    def print_data(self):
        print("Printing document")


p = printerscanner()

p.scan()
p.print_data()
