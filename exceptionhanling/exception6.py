#working with  default exeptions
try:
    no1=int(input(('1st no :')))
    no2= int(input('2nd no :'))
    print('sum :',no1+no2)
    print('div :',no1/no2)
    print('sub :',no1-no2)
    print('mul : ',no1*no2)
except:                                   # default exceptions it handle all exceptions
    print("invalid inputs")
print('thanks')