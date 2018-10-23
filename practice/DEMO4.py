class movie_ticket:
    adult_cost=200
    child_cost=adult_cost/2
    amount=(adult_cost+child_cost)
    gst=amount*0.10
    total_cost=amount+gst
    show_time='9 AM'
    ending_time='12 AM'
    def calculate(self):
        self.adults=int(input('enter no of adults:'))
        self.childs=int(input('enter no of childs:'))
        self.adult_cost=self.adults*movie_ticket.adult_cost
        self.child_cost=self.childs*movie_ticket.child_cost
        self.gst=(self.adult_cost+self.child_cost)*0.10
        self.total_cost=self.adult_cost+self.child_cost+self.gst


class ticket_cost(movie_ticket):
    def show(self):
        print('adults:',self.adults)
        print('childs:',self.childs)
        print('adult cost:',self.adult_cost)
        print('child cost:',self.child_cost)
        print('GST:',self.gst)
        print('total cost',self.total_cost)
        print('show time is:',movie_ticket.show_time)
        print('show ending time:',movie_ticket.ending_time)
m1=ticket_cost()
m1.calculate()
m1.show()
print('------------------------')
m2=ticket_cost()
m2.calculate()
m2.show()
