from exceptionhanling.exception7 import *
age=int(input('enter your age: '))
try:
    res=validateAge(age)
    print(age)
    cno=int(input('enter contact number:'))
except ValueError as ve:
    print(ve)
