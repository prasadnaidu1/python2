from pickle import *
import python2.product
x=int(input('enter how many values you want to serilize;'))
f = open('demo3','wb')
for i in range(1,x+1):
    m=int(input('enter id no : '))
    n=input('enter product name : ')
    o=float(input('enter price of the product : '))
    productobj=python2.product.Product(m,n,o)
    dump(productobj,f)
print('serilization is completed')
f.close()