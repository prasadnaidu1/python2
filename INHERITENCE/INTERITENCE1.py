class bank:
    balance=0
    def deposite(self,amount):
        self.balance+=amount
        print('the current balance:',self.balance)
    def withdraw(self,amount):
        self.balance-=amount
        print('after withdraw money the current balance is:',self.balance)
class sbi(bank):
    def payint(self,amount):
        self.balance+=amount
        self.intamt=amount
        print('after adding the interest then the current balance:',self.balance)
s=sbi()
s.deposite(10000)
s.withdraw(2000)
s.payint(1000)

