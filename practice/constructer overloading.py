class customer:
    store_name='prasad provitional store'
    store_add='hyderabad'
    def __init__(self,idno=0,name=None,price=0.0):
        self.cust_idno=idno
        self.cust_name=name
        self.price=price
        self.discount = self.price*0.10
        self.after_disount=self.price-self.discount
        self.servicetax=self.price*0.05
        self.total_price_of_product=(self.price+self.servicetax)+self.discount
    def show(self):
        print('storename:',customer.store_name)
        print('store adderess:',customer.store_add)
        print('customer idno:',self.cust_idno)
        print('customer name:',self.cust_name)
        print('product price:',self.price)
        print('discount of the product:',self.discount)
        print('after discount the product original value:',self.after_disount)
        print('service tax of the product:',self.servicetax)
        print('finally price of the product:',self.total_price_of_product)
c1=customer(1122,'Prasad',30000)
c1.show()
print('=================================')

