class employee:
    comp_name='satya'
    comp_cno=9052766763
    def assign(self,id,name):
        self.idno=id
        self.name=name
    def display(self):
        print('company name:',employee.comp_name)
        print('company contact number:',employee.comp_cno)
        print('employee id number:',self.idno)
        print('employee name:',self.name)
e1=employee()
e1.assign(101,'prasad')
e1.display()
print('--------------------------------------------')
e2=employee()
e2.assign(102,'raju')
e2.display()