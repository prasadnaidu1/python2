a=10
print(a)
def display(name,surname='mukthavarapu',lastname='krishna'):
    global a
    a=1000
    print(a)
    print('name=',name)
    print('surname=',surname)
    print('lastname=',lastname)
def show():
    global b
    b=i+60
    b-=22
    print(b)
def ismail():
    global c

    c =9476
    c+=1
    print(c)
#calling block
display('vamsi')
show()
ismail()

