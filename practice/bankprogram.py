class bank:
    balance=0
    def deposite(self):
        self.amount=int(input('enter amount'))
        self.balance+=self.amount
        self.interest=self.balance*0.05
        if self.balance>=10000:
            print('thanks for maintaining balance in my bank')
            print('you are eligible for taking interst')
            print('this month interest is:',self.interest)
            print('your current balance is:',self.balance+self.interest)
            print('THANKS YOU')
        else:
            print('you are not eligible for talking interst',self.balance)
        if self.balance<=1000:
            print('you have to maintain minimum balance in your bank so u cannot withdaw money')
            print('your current balance:',self.balance)
        else:
            pass
b=bank()
b.deposite()

