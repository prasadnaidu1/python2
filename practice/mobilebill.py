class postpaid:
    company_name='IDEA'
    company_addess='TIRUPATI'
    monthly_minimum_minutes=1000
    each_minute_cost=0.50
    extra_each_minute_cost=0.70
    def __init__(self):
        self.total_customer_talking_minutes=int(input('enter how many minutes customer talked :'))

        self.total_customer_talking_minutes_on_cost=self.total_customer_talking_minutes*postpaid.each_minute_cost

        self.extra_minutes = self.total_customer_talking_minutes - postpaid.monthly_minimum_minutes

        self.extra_minutes_cost = self.extra_minutes * postpaid.extra_each_minute_cost

        self.total_minutes=self.total_customer_talking_minutes

    def display(self):
        if self.total_minutes>=1500:
            print('You Crossed More Than 1500 Minutes So Charges Are Applicable')

            print('The Normal Bill Is : ',self.total_customer_talking_minutes_on_cost)

            print('Your Extra Minutes : ',self.extra_minutes)

            print('Cost Of Each Minute : ',postpaid.extra_each_minute_cost)

            print('Extra Cost On Monthly Bill : ',self.extra_minutes_cost)

            print('The Monthly Bill : ',self.total_customer_talking_minutes_on_cost+self.extra_minutes_cost)

            print('THANKS YOU FOR SUPPORTING TO OUR TEAM')
        else:
            print('Your Talking Minutes Were : ',self.total_customer_talking_minutes)

            print('Cost Of Each Minute Is : ',postpaid.each_minute_cost)

            print('The Monthly Bill : ',self.total_customer_talking_minutes*postpaid.each_minute_cost)

            print('THANKS YOU FOR SUPPORTING TO OUR TEAM')



#calling block

p1=postpaid()

print('OUR COMPANY NAME IS  :  ',postpaid.company_name)

print('OUR COMPANY ADDRESS IS  :  ',postpaid.company_addess)

p1.display()
