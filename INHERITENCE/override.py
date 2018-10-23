class first:
    def calculate(self,x,y):
        self.x=x
        self.y=y
        print('the sum  is : ', self.x+self.y)
        print('the sub is : ' ,self.x-self.y)

class second(first):
    def calculate(self,x,y):

        super().calculate(x,y)
        print('the mul  is : ', self.x*self.y)
        print('the div is : ' ,self.x/self.y)
class third(second):
    def calculate(self,x,y):

        super().calculate(x, y)
        print('the floor div  is : ', self.x//self.y)
        print('the modulo is : ' ,self.x%self.y)
print('This is first class')
f1=first()
f1.calculate(15,2)
print('==================================================================')
print('This is second class')
s1=second()
s1.calculate(15,2)
print('=========================================================================')
print('This is third class')
t1=third()
t1.calculate(15,2)
print('==========================================================================')