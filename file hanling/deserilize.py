from pickle import *
from python2.product import *
f=open('demo3','rb')
while True:
    try:
        i=load(f)
        print(i)
    except EOFError:

        break
f.close()