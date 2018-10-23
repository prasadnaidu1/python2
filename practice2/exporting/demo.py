a =100       # global variable .
def fun1():
    global a # bcz if you want to use the global inside a function or method we have use a global word.
    a =1000
    print(a)
class fun2:
    x =7677      # static variable or class variable
    def fun3(self,com_name,com_no):      # Instance method.
        y =200  # local variable
        self.company_name =com_name
        self.company_contact =com_no
    def fun4(self):
        print(fun2.x)
        print(self.company_name)
        print(self.company_contact)
        print(fun3.y)

