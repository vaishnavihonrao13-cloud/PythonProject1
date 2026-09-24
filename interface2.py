from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class creditcard(payment):
    def pay(self,amount):
        print("paid RS.",amount,"using credit card")

class upi(payment):
    def pay(self,amount):
        print("paid RS.",amount,"using upi card")

p1=creditcard()
p1.pay(100)
p2=upi()
p2.pay(100)
