 from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def payment(self):
        pass
class branch(bank):
    def payment(self,acount_no,acount_holdername):
        self.acount_no=acount_no
        self.acount_holder_name=acount_holdername

    def show(self,amount):
        self.amount=amount
        print('acount number:',self.acount_no)
        print('acount holder name:',self.acount_holder_name)
        print(self.amount,'is paid to your account')
b1=branch()
b1.payment(112233,'prasad')
b1.show(20000000)






