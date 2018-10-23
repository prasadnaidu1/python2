class company:

    def __init__(self):
        self.emp_id=int(input('enter employee id:'))
        self.emp_name=input('enter employee name:')
        self.gender=input('enter type:')
        self.sal=int(input('enter sal:'))
        self.daily_allowence=self.sal*0.10
        self.human_resource=self.sal*0.05
        self.travelling_allowence=self.sal*0.10
        self.total_salary=self.sal+self.daily_allowence+self.human_resource+self.travelling_allowence
    def display(self):
        print('employee id:',self.emp_id)
        print('employee name',self.emp_name)
        print('gender:',self.gender)
        print('employee salary:',self.sal)
        print('dailyallowences:',self.daily_allowence)
        print('human resourse:',self.human_resource)
        print('travelling allowences:',self.travelling_allowence)
        print('total salary:',self.total_salary)
#calling block
emp=company()
emp.display()
emp1=company()
emp1.display()
