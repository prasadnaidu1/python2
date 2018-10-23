from abc import ABC,abstractmethod
class pizza(ABC):
    @abstractmethod
    def calculatebill(self):
        pass
class vezpizza(pizza):
    customer_name=input('enter cutomer name:')
    customer_idno=int(input('enter your id:'))
    def calculatebill(self,actualcost,m):
        self.actual_cost =actualcost
        self.m=m
        self.discount=(self.m*self .actual_cost)*0.10
        self.total_cost=(self.m*self.actual_cost)-self.discount
        if self.total_cost>1000:
            print('discount',self.discount)
            print('total cost of vezpizza:',self.total_cost)
        else:
            print('total cost of vezpizza:', self.m*self.actual_cost)
class nonvezpizza(pizza):
    def calculatebill(self, actualcost, n):
        self.actual_cost = actualcost
        self.n = n
        self.discount1 = (self.n*self.actual_cost)*0.05
        self.total_cost1 = (self.n*self.actual_cost) - self.discount1
        if self.total_cost1 > 2000:
            print('discount', self.discount1)
            print('total cost of vezpizza:', self.total_cost1)
        else:
            print('total cost of vezpizza:', self.n*self.actual_cost)
v1=vezpizza()
print('customer name:',vezpizza.customer_name)
print('customer id no:',vezpizza.customer_idno)
v1.calculatebill(400,3)
print('========================================================')
print('this is non veg details')
v2=nonvezpizza()
v2.calculatebill(1000,1)



