class employee:
    def __init__(self,amount):
        self.amount=amount
    def dispaly(self):
        print('The Basic Salary :', self.amount)
class bonus(employee):
    def __init__(self,amount):
        super().__init__(amount)
        self.bonus=self.amount*0.05
        self.total_salary=self.amount+self.bonus
    def dispaly(self):
        super().dispaly()
        print('Employee Bonus On Basic Salary :',self.bonus)
        print('Employee Total Salary:',self.total_salary)
class promotion(bonus):
    def __init__(self,amount):
        super().__init__(amount)
        self.promotion=self.amount*0.20
        self.total_salary1=self.total_salary+self.promotion
    def dispaly(self):
        super().dispaly()
        print('Employee  Promotion On Salary: ',self.promotion)
        print('The Final Salary:',self.total_salary1)
print('AT THE STARTING TIME')
e1=employee(20000)
e1.dispaly()
print('========================================')
print('AFTER ONE YEAR I GOT BONUS IN MY OOMPANY ')
b1=bonus(20000)
b1.dispaly()
print('========================================')
print('AFTER THREE YEARS I GOT PROMOTION IN MY COMPANY AS A TEAM LEADER')
p1=promotion(20000)
p1.dispaly()

