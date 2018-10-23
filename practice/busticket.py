class  ticket:
    adult_cost=37555.0
    child_cost=adult_cost/3
    amount=(adult_cost+child_cost)
    discount=amount*0.10
    sub_total=amount-discount
    service_tax=sub_total*0.07
    total_cost=(sub_total+service_tax)
    def __init__(self):
        self.adults=int(input('enter no of adults:'))
        self.childs=int(input('enter no of childs'))
        self.amount1=ticket.adult_cost*self.adults
        self.amount2=ticket.child_cost*self.childs
class ticket1(ticket):
    def details(self):
        self.total=self.amount1+self.amount2
        self.discount=self.total*0.10
        self.sub_total=self.total-self.discount
        self.service_tax=self.sub_total*0.07
        self.total_cost=self.sub_total+self.service_tax
    def display(self):
        print('no of adults:',self.adults)
        print('no of childs:',self.childs)
        print('adult_cost:',self.adults*ticket.adult_cost)
        print('child_cost:',self.childs*ticket.child_cost)
        print('total:',self.total)
        print('discount:',self.discount)
        print('sub_total:',self.sub_total)
        print('service_tax:',self.service_tax)
        print('total cost:',self.total_cost)
#calling block
t1=ticket1()
t1.details()
t1.display()
print('-----------------------------------------')
t2=ticket1()
t2.details()
t2.display()
print('-----------------------------------')

