from threading import *
from time import *
class X(Thread):
    def run(self):
        for i in range(1,21):
            print(i)
            sleep(2)
class Y(Thread):
    def run(self):
        x = X()
        x.start()
        for i in range(21,41):
            print(i)
            sleep(3)
            if i==30:
                x.join()
y=Y()
y.start()



