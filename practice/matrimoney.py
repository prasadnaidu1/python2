import datetime
class matrimoney:
    matrimoney_name='telugu matrimoney'
    address='bangalore'
    td=datetime.datetime.today()
    tdt=datetime.date.today()
    d1, m1, y1 = [int(x) for x in input('enter your date of birth(dd/mm/yyy)').split('/')]
    date_of_birth = datetime.date(year=y1, month=m1, day=d1)
    def select(self):
        self.name=input('enter your good name:')
        self.gender=input('enter your gender:')
        self.mobile=int(input('enter your mobile number:'))
        self.age=matrimoney.tdt-matrimoney.date_of_birth
        self.days=int(self.age.days)
        self.age1=self.days//365
        self.region=input('enter your living region:')
        self.male_age=self.age1
        self.female_age=self.age1
        self.male_age_charges=30000
        self.female_age_charges = 20000
        self.additional_charges=20000
        self.total_cost_of_male=self.male_age_charges+self.additional_charges
        self.total_cost_of_female = self.female_age_charges + self.additional_charges
        if self.gender=='male' and self.male_age>=30:
            print('company name:', matrimoney().matrimoney_name)
            print('comapny address:', matrimoney().address)
            print('name:', self.name)
            print('gender:', self.gender)
            print('date of birth:', self.date_of_birth)
            print('mobile:', self.mobile)
            print('region:', self.region)
            print(' male age is:', self.male_age)
            print('actual charges for male=',self.male_age_charges)
            print('additional charges of male=',self.additional_charges)
            print('total charges of male=',self.male_age_charges+self.additional_charges)
        else:
            print('total cost of male=',self.male_age_charges)
        if self.gender=='female'and  self.female_age>=25:
            print('company name:', matrimoney().matrimoney_name)
            print('comapny address:', matrimoney().address)
            print('name:', self.name)
            print('gender:', self.gender)
            print('date of birth:', self.date_of_birth)
            print('mobile:', self.mobile)
            print('region:', self.region)
            print('female age is:', self.female_age)
            print('actual charges for female=', self.female_age_charges)
            print('additional charges of female=', self.additional_charges)
            print('total charges of female=', self.female_age_charges + self.additional_charges)
        else:
            pass
class management(matrimoney):
    def show(self):
        pass
 #calling block
print('welcome to telugu matrimony')
m1=management()
m1.select()
m1.show()




