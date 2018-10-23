
try:
    no1=int(input('1st no :'))
    no2=  int(input('2nd no: '))
    print('sum : ', no1 + no2)
    print('div :', no1 / no2)
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print(ve)
else:
    print('mul : ', no1 * no2)
    print('sub :', no1 - no2)
print("Thanks")