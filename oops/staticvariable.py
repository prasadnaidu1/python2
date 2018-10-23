class employee:
    comp_name='satya' #static varaible
    comp_address='hyd' #static varaible
    def display(self):
        print('companyname:',employee.comp_name)
        print('companyaddress:',employee.comp_address)
#creating object
emp=employee()
emp.display()