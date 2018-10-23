class employee:
    def assign(self,idno=0,name=None,sal=0.0):
        self.idno=idno
        self.name=name
        self.sal=sal
    def display(self):
        print('employee idno:',self.idno)
        print('employee name:',self.name)
        print('employee sal:',self.sal)
e1=employee()
e1.assign()
e1.display()
print('=======================================')
e2=employee()
e2.assign(102)
e2.display()
print('=======================================')
e3=employee()
e3.assign(103,'ravi',125000)
e3.display()
print('=======================================')
e4=employee()
e4.assign(sal=34000,idno=1122,name='raju')
e4.display()
print('=======================================')
e5=employee()
e5.assign(name='prasad',sal=125000)

e5.display()
e5.idno=2233
e5.display()