class employee:
    comp_name="satya"
    comp_cno=9052766763
    def assign(self):
        self.idno=101
        self.name="prasad"
    def display(self):
        print(self.idno)
        print(self.name)
        print(employee.comp_name)
        print(employee.comp_cno)
e1=employee()
e1.assign()
e1.display()