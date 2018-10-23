class Demo:
    a =10               # static variable
    def display(self,id,name): #  self is a Instance variable and id,name is a local variable.
        self.idno =id
        self.idname =name
    def show(self):
        print(Demo.a)
        print(self.idno)
        print(self.idname)
#calling block
d =Demo()
d.display(9477,'ismail')
d.show()