class employee:
    company_name='satya technologies'
    company_cno=9052766763
    def assign(self,id=0,name=None,sal=0,pf=0,da=0,hra=0):
        self.idno=id
        self.name=name
        self.sal=sal
        self.pf=pf
        self.da=da
        self.hra=hra
        self.total_pf=self.sal*self.pf
        self.total_da=self.sal*self.da
        self.total_hra=self.sal*self.hra
        self.total_sal=self.sal+self.total_pf+self.total_da+self.total_hra
    def show(self):
        print('employee idno:',self.idno)
        print('employee name:',self.name)
        print('basic salary:',self.sal)
        print('profitfund:',self.total_pf)
        print('daily allowences:',self.total_da)
        print('human allowences:',self.total_hra)
        print('employee total salary:',self.total_sal)
e1=employee()
print('company name:',employee.company_name)
print('company contactno:',employee.company_cno)
e1.assign()
e1.show()
print('==========================================')
e2=employee()
print('company name:',employee.company_name)
print('company contactno:',employee.company_cno)
e2.assign(id=1122,name='prasad')
e2.show()
print('==========================================')
e3=employee()
print('company name:',employee.company_name)
print('company contactno:',employee.company_cno)
e3.assign(id=101,name='prasad',sal=120000,pf=0.05,da=0.10,hra=0.05)
e3.show()
print('========================')
e3.idno=6677
e3.name='Ravi'
e3.show()
print('============================================')




