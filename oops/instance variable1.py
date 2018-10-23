class employee:
    def assign(self):
        self.idno=101
        self.name='satya'
    def display(self):
        print(self.idno)
        print(self.name)
emp=employee()
emp.assign()
emp.display()