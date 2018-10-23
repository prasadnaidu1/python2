#example progarm on nested try block with except block
try:
    no1=int(input('1st no :'))
    no2=  int(input('2nd no: '))
    print('sum : ', no1 + no2)

    try:
            print('div :', no1 / no2)
    except ZeroDivisionError as zde:
            print("Division not possible  becauseyou entered invalid input its not divided by zero")
    print('mul : ', no1 * no2)
    print('sub :', no1 - no2)
except ValueError as ve:
    print("only it allows integer values ")
print("Thanks")