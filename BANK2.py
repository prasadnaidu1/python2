from abc import ABC,abstractmethod
class bank:
    @abstractmethod
    def acount(self):
        pass
class branch(bank):
    def acount(self):
        self.aadhar=input('enter your aadhar no:')
        self.voter =str(input('enter your voter no:'))
        self.amount=float(input('enter your amount:'))
        if len(self.aadhar)==12 and self.amount>= 1000:
            print('your aadhar verification is succesfully')
            print('Thanks you for maintaining your minimum balance')
            print('the acount will be opened in our bank very shortly')
        else:
            print('your addhar verification failed')
        if len(self.voter)==6 and self.amount>=1000:
                print('your voter verification is  suceesfully' )
                print('Thanks you for maintaining your minimum balance')
                print('the acount will be opened in our bank very shortly')
        else:
                print('your voter id number is not correct')
#calling block
b=branch()
b.acount()
