from threading import *
from time import *
def fun1():
    for i in range(1,50):
        print(i)
        sleep(2)
def fun2():
    while True:
        print("hello")
        sleep(6)
t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()
t2.daemon=True
t2.start()
t2.join()