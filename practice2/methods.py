class ismail:
    a =68                      # static or class variable.
    def fun1(self,b):        # self is  Instance variable , b is a local variable
        self.b =200
    def kiran(self):
        print(self.b)
        self.b+=20
        f =ismail.a                # using the class variables in instance method.
        self.a+=2
        print(self.a)
    @classmethod
    def anji(cls,i):
        cls.a +=100
    @ staticmethod
    def muthu(i,j):
        print(i)
        print(j)
#calling block
m =ismail()
#m.muthu(76,77)
#m.kiran()
#m.anji(66)
m.fun1(23)

