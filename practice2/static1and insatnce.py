class Demo:
    a =10               # static variable
    def display(self): #  self is a Instance variable and id,name is a local variable.
        self.id =101
        self.name ='basha'
    def show(self):
        print(Demo.a)
        print(self.id)
        print(self.name)

#calling block
d =Demo()
d.display()
d.show()