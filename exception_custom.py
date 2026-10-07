class BankException(Exception):
    def __init__(self,msg):
        self.msg=msg
class Bank:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amt):
        if self.balance-amt<0:
            raise BankException("insufficient balance")
        else:
            self.balance-=amt
b=Bank(40000)
try:
    b.withdraw(100000)
except  Exception as e:
    print(e)
print(b.balance)