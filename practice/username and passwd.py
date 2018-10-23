count=1
while True:
    usename=input('Enter Your Username: ')
    pin = int(input('Enter Your Pin : '))
    if usename=='prasad' and pin==9052:
        print('Your Login Is Success')
        break
    else:
        count+=1
        if count>3:
            print('You Crossed Today Three Attempts ')
            print('Account Was Blocked,Try Again Tomorrow')
            break
    print('Your Login Failed')
    ans=int(input('To Continue For Press 1: '))
    if ans==1:
        continue
    else:
        break
print('THANKS')




