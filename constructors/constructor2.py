class employee:
    def __init__(self,idno, name):
        self.emp_idno=idno
        self.emp_name=name
    def show(self):
        print('employee id no is:',self.emp_idno)
        print('employee name is:',self.emp_name)
emp=employee(101,'prasad')
emp.show()
print('=========================================================')
emp1=employee(102,'chowdary')
emp1.show()
