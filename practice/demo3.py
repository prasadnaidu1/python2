class bank:
    bank_name="state bank of india"
    ifsc_code="SBIN0002703"
    branch_add="tirupati"
    branch_code=1234
    def calculate(self,amount):
        self.amount=amount
        self.accont_holdername=input('enter name:')
        self.account_number=int(input('enter account number:'))
    def show(self):
        print('account holder name:',self.accont_holdername)
        print('acount numebr:',self.account_number)
        print('name of the bank:',bank.bank_name)
        print('bank IFSC code:',bank.ifsc_code)
        print('bank address:',bank.branch_add)
        print('bank branch code:',bank.branch_code)
        print(self.amount,'deposited to',self.account_number)
b1=bank()
b1.calculate(50000)
b1.show()



