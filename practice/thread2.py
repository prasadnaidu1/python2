from threading import *
from time import*
class x(Thread):
    def run(self):
        for i in range(1,50):
            print(i)
            sleep(2)

class y(Thread):
    def run(self):
        for j in range(50,100):
            print(j)
            sleep(3)
#calling block
xobj=x()
yobj=y()
xobj.start()
yobj.start()