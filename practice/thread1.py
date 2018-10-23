
from threading import Thread
from time import *
class X:
    def fun1(self):
         for i in range(1,11):
           print(i)
           sleep(2)
class Y:
    def fun2(self):
        for j in range(11,21):
          print(j)
          sleep(2)
    #calling block
x=X()
y=Y()
t1=Thread(target=x.fun1)
t2=Thread(target=y.fun2)
t1.start()
t2.start()
