class mobile_bill:
    def __init__(self):
        self.monthly_bill=int(input('enter monthly bill : '))
    def show(self):
        print('Monthly bill :',self.monthly_bill)
class first(mobile_bill):
    def __init__(self):
        super().__init__()
        self.roaming_charges = self.monthly_bill * 0.02
        self.total_bill=self.monthly_bill+self.roaming_charges
    def show(self):
        super().show()
        print('Roaming On Monthly bill :', self.roaming_charges)
        print('Total On Monthly bill :)',self.total_bill)
class second(first):
    def __init__(self):
        super().__init__()
        self.gst=self.monthly_bill*0.06
        self.final_bill_of_month=self.monthly_bill+self.roaming_charges+self.gst
    def show(self):
        super().show()
        print('Goods Service Tax is :',self.gst)
        print('Final Bill On Present Days :',self.final_bill_of_month)
#calling block
m1=mobile_bill()
print('AT THE STARTING TIME')
m1.show()
print('==========================================')
f1=first()
print('AFTER INTRODUSING TAX ON MOBILE BILLS')
f1.show()
print('==========================================')
s1=second()
print('AFTER INTRODUSING GOOD AND SERVICE TAX')
s1.show()
print('============================================')