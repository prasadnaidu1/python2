class employee:
    company_name='TCS'
    department='PRODUCTION'
    disighnation='operators'
    def details(self,):
        self.id=int(input('enter id:'))
        self.name=input('enter name:')
        self.sal=int(input('enter sal:'))
    def show(self):
        print('employeeid:',self.id)
        print('employeename:',self.name)
        print('employeesal',self.sal)
        print('company_name:', employee.company_name)
        print('department:', employee.department)
        print('disighnation:', employee.disighnation)
emp=employee()
emp.details()
emp.show()
print('---------------------------------')
emp1=employee()
emp1.details()
emp1.show()










