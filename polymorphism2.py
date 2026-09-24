class payment:
    def pay(self):
        pass
class cash(payment):
    def pay(self):
        print("cash")
class upi(payment):
    def pay(self):
        print("upi")
cash=cash()
upi=upi()
upi.pay()
cash.pay()