
try:
    x=int(input('enter your amount:'))
    if x>=50000:
       raise (None)
    else:
       print('your money deposited')
except:
    print('you dont have permission to deposite this much of money')
finally:
 print('thanks you')



